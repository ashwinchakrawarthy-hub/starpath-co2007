"""RAG pipeline and retrieval unit tests for STARPath."""
import unittest
from app.retriever import retriever_instance
from app.rag import process_question
from app.llm import simplify_answer_text


class TestRAGPipeline(unittest.TestCase):

    def test_chunks_loaded(self):
        """Verify knowledge base has loaded the approved page chunks."""
        self.assertGreaterEqual(len(retriever_instance.chunks), 8)

    def test_in_scope_retrieval(self):
        """Verify in-scope question retrieves correct STAR page."""
        results, is_out_of_scope, score = retriever_instance.retrieve("What is the STAR programme?")
        self.assertFalse(is_out_of_scope)
        self.assertGreater(len(results), 0)
        self.assertIn("star-programme", results[0]["url"])

    def test_honest_refusal_on_out_of_scope(self):
        """Verify out-of-scope query triggers honest refusal."""
        res = process_question("What is the price of a pint of beer in the student bar?")
        self.assertTrue(res["is_honest_refusal"])
        self.assertIn("could not find information", res["answer"].lower())
        self.assertIn("inclusivesupport@uclan.ac.uk", res["answer"])

    def test_crisis_guardrail_integration(self):
        """Verify crisis query bypasses LLM and returns Wellbeing contacts."""
        res = process_question("I feel like killing myself right now")
        self.assertTrue(res["is_crisis"])
        self.assertIn("01772 893020", res["answer"])
        self.assertIn("116 123", res["answer"])

    def test_plain_english_simplification(self):
        """Verify simplification rewrites formal terminology."""
        sample = "Eligible offer-holders receive reasonable adjustments in halls of residence."
        simplified = simplify_answer_text(sample)
        self.assertIn("accepted students", simplified.lower())
        self.assertIn("student flats on campus", simplified.lower())

    def test_keyword_baseline_search(self):
        """Verify baseline search returns passage without LLM."""
        res = retriever_instance.keyword_baseline_search("Disabled Students Allowance DSA grant")
        self.assertFalse(res["is_honest_refusal"])
        self.assertIn("dsa", res["source_url"].lower())
        self.assertEqual(res["method"], "Simple Keyword Match (Baseline)")


if __name__ == "__main__":
    unittest.main()
