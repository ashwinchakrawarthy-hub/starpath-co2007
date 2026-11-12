"""Privacy & Anonymity module for STARPath.

Redacts Personally Identifiable Information (PII) including emails, phone numbers,
student ID numbers, postcodes, and credit card numbers before any LLM prompt is constructed.
Ensures zero storage of user question text or identity.
"""
import re
from typing import Tuple, List

# Regular expression patterns for PII detection
EMAIL_REGEX = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')
# UK and international phone numbers (e.g. +44 7911 123456, 07123456789, 01772 123456)
PHONE_REGEX = re.compile(r'(?:\+44\s*(?:\(0\)\s*)?|\b0)[1-9]\d{1,4}(?:[\s-]?\d{2,4}){1,3}\b')
# UCLan Student ID numbers (G-numbers like G12345678 or 8-digit numbers)
STUDENT_ID_REGEX = re.compile(r'\b([Gg]\d{7,8}|\b\d{8}\b)')
# UK Postcodes (e.g. PR1 2HE, M13 9PL)
POSTCODE_REGEX = re.compile(r'\b[A-Z]{1,2}\d[A-Z0-9]?\s*\d[A-Z]{2}\b', re.IGNORECASE)
# Credit/Debit Card numbers (16 digits)
CARD_REGEX = re.compile(r'\b(?:\d{4}[-\s]?){3}\d{4}\b')


def redact_pii(text: str) -> Tuple[str, bool, List[str]]:
    """Redact personal details from user input before sending to LLM.
    
    Returns:
        redacted_text: Sanitized string with placeholders
        pii_detected: Boolean indicating whether any PII was stripped
        redactions: List of types of PII redacted
    """
    if not text:
        return text, False, []

    redacted = text
    detected_types = []

    if EMAIL_REGEX.search(redacted):
        redacted = EMAIL_REGEX.sub("[EMAIL REDACTED FOR PRIVACY]", redacted)
        detected_types.append("Email address")

    if PHONE_REGEX.search(redacted):
        redacted = PHONE_REGEX.sub("[PHONE NUMBER REDACTED]", redacted)
        detected_types.append("Phone number")

    if STUDENT_ID_REGEX.search(redacted):
        redacted = STUDENT_ID_REGEX.sub("[STUDENT ID REDACTED]", redacted)
        detected_types.append("Student ID number")

    if CARD_REGEX.search(redacted):
        redacted = CARD_REGEX.sub("[CARD NUMBER REDACTED]", redacted)
        detected_types.append("Payment card number")

    if POSTCODE_REGEX.search(redacted):
        redacted = POSTCODE_REGEX.sub("[POSTCODE REDACTED]", redacted)
        detected_types.append("Postcode")

    pii_found = len(detected_types) > 0
    return redacted, pii_found, detected_types


def sanitize_log_message(event_type: str, status: str, duration_ms: float) -> str:
    """Format structured anonymous log entries without any user question content or identifiers."""
    return f"[STARPath-Event] type={event_type} status={status} duration_ms={duration_ms:.1f}"
