"""Privacy and PII Redaction unit tests for STARPath."""
import unittest
from app.privacy import redact_pii


class TestPrivacyFilter(unittest.TestCase):

    def test_email_redaction(self):
        text = "Hello my name is Alex and my email is student123@uclan.ac.uk, please contact me."
        redacted, detected, types = redact_pii(text)
        self.assertTrue(detected)
        self.assertIn("Email address", types)
        self.assertNotIn("student123@uclan.ac.uk", redacted)
        self.assertIn("[EMAIL REDACTED FOR PRIVACY]", redacted)

    def test_uk_phone_redaction(self):
        phones = [
            "My mobile is 07123456789 can you call me?",
            "Call me at +44 7911 123456 please.",
            "My home number is 01772 123456."
        ]
        for p in phones:
            redacted, detected, types = redact_pii(p)
            self.assertTrue(detected, f"Failed on {p}")
            self.assertIn("Phone number", types)
            self.assertIn("[PHONE NUMBER REDACTED]", redacted)

    def test_student_id_redaction(self):
        text = "My UCLan student ID number is G20987654 and my friend is 20987654."
        redacted, detected, types = redact_pii(text)
        self.assertTrue(detected)
        self.assertIn("Student ID number", types)
        self.assertNotIn("G20987654", redacted)
        self.assertIn("[STUDENT ID REDACTED]", redacted)

    def test_postcode_redaction(self):
        text = "I live at flat 4 in PR1 2HE Preston."
        redacted, detected, types = redact_pii(text)
        self.assertTrue(detected)
        self.assertIn("Postcode", types)
        self.assertNotIn("PR1 2HE", redacted)

    def test_clean_text_no_false_redactions(self):
        text = "What is the STAR programme and is accommodation free?"
        redacted, detected, types = redact_pii(text)
        self.assertFalse(detected)
        self.assertEqual(len(types), 0)
        self.assertEqual(text, redacted)


if __name__ == "__main__":
    unittest.main()
