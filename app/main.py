"""FastAPI web application for STARPath - Accessible STAR Programme Assistant."""
import csv
import time
from pathlib import Path
from typing import List, Optional
from fastapi import FastAPI, Request, Query
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field

from app.config import (
    APP_NAME,
    APP_SUBTITLE,
    LLM_PROVIDER,
    CHUNKS_PATH,
    GLOSSARY_PATH,
    EVAL_QUESTIONS_PATH,
    BASE_DIR
)
from app.rag import process_question, GLOSSARY_ITEMS
from app.retriever import retriever_instance
from app.llm import simplify_answer_text

app = FastAPI(
    title=APP_NAME,
    description="Accessible, privacy-first Q&A assistant for UCLan's STAR Programme (CO2007 Agile Team Project)",
    version="1.0.0"
)

# Setup templates and static directory
APP_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = APP_DIR / "templates"
STATIC_DIR = APP_DIR / "static"

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


# Pydantic Request / Response Models
class AskRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=1000, description="The user's question")


class SimplifyRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Answer text to simplify")


# Web Page Routes
@app.get("/", response_class=HTMLResponse)
async def index_page(request: Request):
    """Main Q&A Assistant Chat Interface."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "app_name": APP_NAME,
            "app_subtitle": APP_SUBTITLE,
            "llm_provider": LLM_PROVIDER,
            "glossary_count": len(GLOSSARY_ITEMS),
            "total_chunks": len(retriever_instance.chunks)
        }
    )


@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    """Student Ambassador sharing page with printable QR card mock-up."""
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={
            "app_name": APP_NAME,
            "app_subtitle": APP_SUBTITLE,
            "llm_provider": LLM_PROVIDER
        }
    )


@app.get("/evaluation", response_class=HTMLResponse)
async def evaluation_page(request: Request):
    """Support team evaluation dashboard (RAG vs Keyword Baseline)."""
    return templates.TemplateResponse(
        request=request,
        name="evaluation.html",
        context={
            "app_name": APP_NAME,
            "app_subtitle": APP_SUBTITLE,
            "llm_provider": LLM_PROVIDER
        }
    )


# API Endpoints
@app.post("/api/ask")
async def api_ask(req: AskRequest):
    """Process a question through the full RAG pipeline."""
    result = process_question(req.question)
    return JSONResponse(content=result)


@app.post("/api/simplify")
async def api_simplify(req: SimplifyRequest):
    """Rewrite text in plain, simple English for international students."""
    simplified = simplify_answer_text(req.text)
    return JSONResponse(content={"simplified_text": simplified})


@app.get("/api/glossary")
async def api_glossary():
    """Retrieve full plain-English university glossary for international students."""
    return JSONResponse(content={"glossary": GLOSSARY_ITEMS, "total": len(GLOSSARY_ITEMS)})


@app.get("/api/baseline")
async def api_baseline(q: str = Query(..., description="Query for keyword baseline search")):
    """Run pure keyword baseline search (no LLM synthesis)."""
    result = retriever_instance.keyword_baseline_search(q)
    return JSONResponse(content=result)


@app.get("/api/evaluate")
async def api_evaluate():
    """Run automated evaluation over all test questions comparing RAG vs Baseline."""
    if not EVAL_QUESTIONS_PATH.exists():
        return JSONResponse(content={"error": "eval_questions.csv not found"}, status_code=404)

    results = []
    rag_correct = 0
    baseline_correct = 0
    total_in_scope = 0
    total_out_scope = 0
    total_crisis = 0
    crisis_handled_correctly = 0
    honest_refusal_correct = 0

    with open(EVAL_QUESTIONS_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid = row.get("id")
            category = row.get("category")
            question = row.get("question", "")
            expected_url = row.get("expected_source_url", "")
            expected_answer = row.get("expected_answer_summary", "")
            is_in_scope = row.get("is_in_scope", "true").lower() == "true"
            is_crisis = row.get("is_crisis", "false").lower() == "true"

            # 1. Run RAG Pipeline
            rag_res = process_question(question)
            
            # 2. Run Keyword Baseline
            baseline_res = retriever_instance.keyword_baseline_search(question)

            # Evaluate RAG
            rag_pass = False
            if is_crisis:
                total_crisis += 1
                if rag_res["is_crisis"]:
                    crisis_handled_correctly += 1
                    rag_pass = True
            elif not is_in_scope:
                total_out_scope += 1
                if rag_res["is_honest_refusal"]:
                    honest_refusal_correct += 1
                    rag_pass = True
            else:
                total_in_scope += 1
                # In-scope: check if expected source URL was retrieved
                retrieved_urls = [s["url"] for s in rag_res.get("sources", [])]
                if expected_url in retrieved_urls and not rag_res["is_honest_refusal"]:
                    rag_correct += 1
                    rag_pass = True

            # Evaluate Baseline
            baseline_pass = False
            if is_crisis or not is_in_scope:
                # Baseline doesn't have safety or LLM honest refusal guard
                baseline_pass = baseline_res.get("is_honest_refusal", False)
            else:
                if baseline_res.get("source_url") == expected_url:
                    baseline_correct += 1
                    baseline_pass = True

            results.append({
                "id": qid,
                "category": category,
                "question": question,
                "expected_answer": expected_answer,
                "expected_source_url": expected_url,
                "is_in_scope": is_in_scope,
                "is_crisis": is_crisis,
                "rag_pass": rag_pass,
                "rag_answer": rag_res["answer"][:180] + "...",
                "rag_sources": [s["title"] for s in rag_res.get("sources", [])],
                "rag_is_crisis": rag_res["is_crisis"],
                "rag_is_honest_refusal": rag_res["is_honest_refusal"],
                "baseline_pass": baseline_pass,
                "baseline_matched_passage": baseline_res.get("matched_passage", "")[:120] + "..."
            })

    total_questions = len(results)
    rag_total_success = sum(1 for r in results if r["rag_pass"])
    baseline_total_success = sum(1 for r in results if r["baseline_pass"])

    summary = {
        "total_questions": total_questions,
        "in_scope_count": total_in_scope,
        "out_of_scope_count": total_out_scope,
        "crisis_count": total_crisis,
        "rag_accuracy_pct": round((rag_total_success / total_questions) * 100, 1),
        "baseline_accuracy_pct": round((baseline_total_success / total_questions) * 100, 1),
        "rag_in_scope_accuracy_pct": round((rag_correct / (total_in_scope or 1)) * 100, 1),
        "baseline_in_scope_accuracy_pct": round((baseline_correct / (total_in_scope or 1)) * 100, 1),
        "safety_guardrail_success_pct": round((crisis_handled_correctly / (total_crisis or 1)) * 100, 1),
        "honest_refusal_success_pct": round((honest_refusal_correct / (total_out_scope or 1)) * 100, 1),
        "what_llm_adds": "RAG provides grounded conversational synthesis, honest refusal for out-of-scope queries, and safety intervention, whereas keyword search frequently retrieves irrelevant passages or fails on paraphrased queries.",
        "results": results
    }
    return JSONResponse(content=summary)


@app.get("/health")
async def health_check():
    """Health check endpoint for cloud monitoring."""
    return {
        "status": "healthy",
        "app": APP_NAME,
        "version": "1.0.0",
        "llm_provider": LLM_PROVIDER,
        "chunks_indexed": len(retriever_instance.chunks),
        "glossary_terms": len(GLOSSARY_ITEMS)
    }
