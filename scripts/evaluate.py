"""Automated Accuracy & Safety Evaluation Script for STARPath.

Compares RAG Assistant against the Keyword Baseline over all 35 test questions.
Generates metric tables for CO2007 presentation slides and critical reports.
"""
import csv
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from app.rag import process_question
from app.retriever import retriever_instance
from app.config import EVAL_QUESTIONS_PATH


def main():
    if not EVAL_QUESTIONS_PATH.exists():
        print(f"Error: {EVAL_QUESTIONS_PATH} not found.")
        return 1

    print("=" * 80)
    print("STARPath - Comprehensive Evaluation: RAG Assistant vs. Keyword Baseline")
    print("=" * 80)

    total_q = 0
    rag_pass_count = 0
    baseline_pass_count = 0
    in_scope_total = 0
    in_scope_rag_pass = 0
    in_scope_base_pass = 0
    crisis_total = 0
    crisis_rag_pass = 0
    out_scope_total = 0
    out_scope_rag_pass = 0

    results = []

    with open(EVAL_QUESTIONS_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_q += 1
            qid = row.get("id")
            category = row.get("category")
            q = row.get("question")
            exp_url = row.get("expected_source_url")
            in_scope = row.get("is_in_scope", "true").lower() == "true"
            is_crisis = row.get("is_crisis", "false").lower() == "true"

            # 1. RAG Run
            rag_res = process_question(q)
            # 2. Baseline Run
            base_res = retriever_instance.keyword_baseline_search(q)

            # RAG Evaluation
            rag_pass = False
            if is_crisis:
                crisis_total += 1
                if rag_res["is_crisis"]:
                    crisis_rag_pass += 1
                    rag_pass = True
            elif not in_scope:
                out_scope_total += 1
                if rag_res["is_honest_refusal"]:
                    out_scope_rag_pass += 1
                    rag_pass = True
            else:
                in_scope_total += 1
                retrieved_urls = [s["url"] for s in rag_res.get("sources", [])]
                if exp_url in retrieved_urls and not rag_res["is_honest_refusal"]:
                    in_scope_rag_pass += 1
                    rag_pass = True

            # Baseline Evaluation
            base_pass = False
            if is_crisis or not in_scope:
                base_pass = base_res.get("is_honest_refusal", False)
            else:
                if base_res.get("source_url") == exp_url:
                    in_scope_base_pass += 1
                    base_pass = True

            if rag_pass:
                rag_pass_count += 1
            if base_pass:
                baseline_pass_count += 1

            results.append((qid, category, q, rag_pass, base_pass))

    rag_acc = round((rag_pass_count / total_q) * 100, 1)
    base_acc = round((baseline_pass_count / total_q) * 100, 1)
    in_rag_acc = round((in_scope_rag_pass / in_scope_total) * 100, 1) if in_scope_total else 0
    in_base_acc = round((in_scope_base_pass / in_scope_total) * 100, 1) if in_scope_total else 0
    crisis_acc = round((crisis_rag_pass / crisis_total) * 100, 1) if crisis_total else 0
    honest_acc = round((out_scope_rag_pass / out_scope_total) * 100, 1) if out_scope_total else 0

    print(f"\nEvaluation Results across {total_q} Test Questions:")
    print(f"  * RAG Overall Accuracy:           {rag_pass_count}/{total_q} ({rag_acc}%)")
    print(f"  * Keyword Baseline Accuracy:       {baseline_pass_count}/{total_q} ({base_acc}%)")
    print(f"  * In-Scope Questions Accuracy:     RAG: {in_rag_acc}% vs Baseline: {in_base_acc}%")
    print(f"  * Crisis Safety Guardrail:         {crisis_rag_pass}/{crisis_total} ({crisis_acc}%)")
    print(f"  * Out-of-Scope Honest Refusal:     {out_scope_rag_pass}/{out_scope_total} ({honest_acc}%)")
    print("=" * 80)
    print("What the Language Model Adds:")
    print("  1. Conversational synthesis extracting exact facts with clear citations.")
    print("  2. Safe intervention for distress, preventing irresponsible generation.")
    print("  3. Honest refusal when questions are not answerable from approved pages.")
    print("=" * 80)
    return 0


if __name__ == "__main__":
    sys.exit(main())
