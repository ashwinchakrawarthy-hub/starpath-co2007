"""RAG Pipeline Orchestrator for STARPath.

Integrates:
1. Crisis and distress detection (Safety guardrail)
2. PII filtering (Privacy & anonymity)
3. Semantic retrieval over approved UCLan page snapshots
4. Honest thresholding for out-of-scope questions
5. LLM grounded answering with source attribution
6. Glossary term matching for international student tooltips
"""
import json
import time
from typing import Dict, Any, List
from app.config import GLOSSARY_PATH, SIMILARITY_THRESHOLD
from app.safety import detect_crisis
from app.privacy import redact_pii
from app.retriever import retriever_instance
from app.llm import generate_rag_answer, simplify_answer_text


def load_glossary() -> List[Dict[str, str]]:
    """Load plain-English glossary terms from disk."""
    if not GLOSSARY_PATH.exists():
        return []
    try:
        with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


GLOSSARY_ITEMS = load_glossary()


def find_glossary_matches(text: str) -> List[Dict[str, str]]:
    """Identify which glossary terms appear in an answer."""
    matches = []
    text_lower = text.lower()
    for item in GLOSSARY_ITEMS:
        term = item.get("term", "")
        if term and term.lower() in text_lower:
            matches.append(item)
    return matches[:6]  # Limit to 6 relevant terms per response to keep UI clean


def process_question(user_question: str) -> Dict[str, Any]:
    """Execute the full STARPath RAG pipeline for a user question.
    
    Returns structured JSON with:
        - answer: Grounded markdown answer
        - sources: List of source citations with URL, title, and collection date
        - is_crisis: Whether safety guardrail triggered
        - is_honest_refusal: Whether question was out-of-scope
        - pii_detected: Whether user question contained personal data
        - pii_types: Redacted PII types
        - matched_glossary: Glossary terms detected in answer
        - provider: LLM provider that generated the response
        - latency_ms: Execution time in milliseconds
    """
    start_time = time.time()
    clean_q = user_question.strip()

    if not clean_q:
        return {
            "answer": "Please enter a question about the UCLan STAR programme, accommodation, or inclusive support services.",
            "sources": [],
            "is_crisis": False,
            "is_honest_refusal": False,
            "pii_detected": False,
            "pii_types": [],
            "matched_glossary": [],
            "provider": "Validation",
            "latency_ms": 0.0
        }

    # Step 1: Safety & Crisis Guardrail Check
    is_crisis, crisis_message, crisis_meta = detect_crisis(clean_q)
    if is_crisis:
        duration_ms = (time.time() - start_time) * 1000
        return {
            "answer": crisis_message,
            "sources": [
                {
                    "title": "UCLan Mental Health and Wellbeing Service",
                    "url": "https://www.lancashire.ac.uk/student-life/support/mental-health-wellbeing",
                    "section": "Emergency and Crisis Support",
                    "date_collected": "2026-11-12"
                }
            ],
            "is_crisis": True,
            "is_honest_refusal": False,
            "pii_detected": False,
            "pii_types": [],
            "matched_glossary": [],
            "provider": "Safety Guardrail (Direct Signposting)",
            "latency_ms": round(duration_ms, 1)
        }

    # Step 2: Privacy Filter (Redact PII before LLM)
    sanitized_q, pii_detected, pii_types = redact_pii(clean_q)

    # Step 3: Retrieval over approved UCLan page chunks
    retrieved_chunks, is_out_of_scope, max_score = retriever_instance.retrieve(sanitized_q)

    # Step 4: Honest Refusal check
    if is_out_of_scope or not retrieved_chunks:
        duration_ms = (time.time() - start_time) * 1000
        honest_answer = (
            "**I could not find information about that in the approved UCLan support pages.**\n\n"
            "As an honest assistant, I do not guess answers when information is not in the official documents. "
            "If your enquiry relates to your individual course or specific personal needs, please contact the "
            "**UCLan Inclusive Support Team** directly:\n"
            "* **Email:** [inclusivesupport@uclan.ac.uk](mailto:inclusivesupport@uclan.ac.uk)\n"
            "* **Phone:** **01772 892593**\n"
            "* **Location:** Student Centre, Preston Campus"
        )
        return {
            "answer": honest_answer,
            "sources": [
                {
                    "title": "UCLan Inclusive Support Service",
                    "url": "https://www.lancashire.ac.uk/student-life/support/inclusive-support",
                    "section": "Enquiries & Appointments",
                    "date_collected": "2026-11-12"
                }
            ],
            "is_crisis": False,
            "is_honest_refusal": True,
            "pii_detected": pii_detected,
            "pii_types": pii_types,
            "matched_glossary": [],
            "provider": "Honest Refusal Guard",
            "latency_ms": round(duration_ms, 1)
        }

    # Step 5: Grounded Answer Generation via Swappable LLM
    answer_text, provider_name = generate_rag_answer(sanitized_q, retrieved_chunks)

    # Step 6: Format source citations
    sources = []
    seen_urls = set()
    for chunk in retrieved_chunks:
        url = chunk.get("url", "")
        if url and url not in seen_urls:
            seen_urls.add(url)
            sources.append({
                "title": chunk.get("page_title", "UCLan Support Page"),
                "url": url,
                "section": chunk.get("section", "General"),
                "date_collected": chunk.get("date_collected", "2026-11-12"),
                "similarity_score": chunk.get("similarity_score", 0.0)
            })

    # Step 7: Match glossary terms
    matched_glossary = find_glossary_matches(answer_text)

    duration_ms = (time.time() - start_time) * 1000
    return {
        "answer": answer_text,
        "sources": sources,
        "is_crisis": False,
        "is_honest_refusal": False,
        "pii_detected": pii_detected,
        "pii_types": pii_types,
        "matched_glossary": matched_glossary,
        "provider": provider_name,
        "latency_ms": round(duration_ms, 1)
    }
