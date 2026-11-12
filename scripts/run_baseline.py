"""Run Keyword Search Baseline on evaluation questions.

Part of CO2007 Deliverable 1 requirements:
Compare the RAG assistant with a simple keyword-search version to demonstrate
what the language model adds over simple passage matching.
"""
import csv
import sys
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from app.retriever import retriever_instance
from app.config import EVAL_QUESTIONS_PATH


def run_baseline():
    if not EVAL_QUESTIONS_PATH.exists():
        print(f"Error: {EVAL_QUESTIONS_PATH} does not exist.")
        return 1

    print("=" * 70)
    print("STARPath - Keyword-Only Baseline Evaluation Run")
    print("=" * 70)

    total = 0
    correct = 0

    with open(EVAL_QUESTIONS_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid = row.get("id")
            question = row.get("question")
            expected_url = row.get("expected_source_url")
            is_in_scope = row.get("is_in_scope", "true").lower() == "true"
            is_crisis = row.get("is_crisis", "false").lower() == "true"
            total += 1

            result = retriever_instance.keyword_baseline_search(question)
            matched_url = result.get("source_url")

            status = "FAIL ✗"
            if is_crisis or not is_in_scope:
                # Baseline has no safety classifier or honest refusal guard
                if result.get("is_honest_refusal"):
                    status = "PASS ✓"
                    correct += 1
            else:
                if matched_url == expected_url:
                    status = "PASS ✓"
                    correct += 1

            print(f"[{qid}] {status} | Q: {question[:50]}...")
            if status == "FAIL ✗":
                print(f"   -> Expected: {expected_url}")
                print(f"   -> Got:      {matched_url}")

    pct = round((correct / total) * 100, 1) if total else 0
    print("-" * 70)
    print(f"Baseline Overall Accuracy: {correct}/{total} ({pct}%)")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    sys.exit(run_baseline())
