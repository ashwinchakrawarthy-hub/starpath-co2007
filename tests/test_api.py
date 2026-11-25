"""FastAPI endpoint unit tests for STARPath."""
import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestAPIEndpoints(unittest.TestCase):

    def test_health_check(self):
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "healthy")
        self.assertEqual(data["app"], "STARPath")

    def test_index_page(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("STARPath", response.text)
        self.assertIn("STAR Residential", response.text)

    def test_about_page(self):
        response = client.get("/about")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Ambassador", response.text)
        self.assertIn("CO2007", response.text)

    def test_evaluation_page(self):
        response = client.get("/evaluation")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Evaluation", response.text)
        self.assertIn("Usability Testing", response.text)

    def test_api_ask_in_scope(self):
        response = client.post("/api/ask", json={"question": "What is the STAR programme?"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("answer", data)
        self.assertGreater(len(data["sources"]), 0)
        self.assertFalse(data["is_crisis"])

    def test_api_ask_crisis(self):
        response = client.post("/api/ask", json={"question": "I feel like killing myself"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["is_crisis"])
        self.assertIn("01772 893020", data["answer"])

    def test_api_simplify(self):
        response = client.post("/api/simplify", json={"text": "Eligible offer-holders receive reasonable adjustments."})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("simplified_text", data)

    def test_api_glossary(self):
        response = client.get("/api/glossary")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreater(data["total"], 20)

    def test_api_baseline(self):
        response = client.get("/api/baseline?q=accommodation+halls")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("matched_passage", data)


if __name__ == "__main__":
    unittest.main()
