"""Safety and Crisis Intervention guardrail for STARPath.

Detects phrases indicating emotional distress, self-harm, or crisis.
If triggered, the system BYPASSES the language model completely and delivers
a fixed, compassionate signposting message directly to human support professionals.
"""
import re
from typing import Tuple, Dict, Any

# Crisis keywords and phrases
CRISIS_PATTERNS = [
    r'\b(?:kill|killing|end|ending)\s+(?:my\s*life|myself)\b',
    r'\b(?:want|wants|wished|wish|wishing)\s+to\s+(?:die|disappear|give\s*up)\b',
    r'\b(?:suicide|suicidal)\b',
    r'\b(?:self[-\s]?harm|self[-\s]?harming|cut\s*myself|cutting\s*myself|hurt\s*myself|hurting\s*myself)\b',
    r'\b(?:overdose|overdosing|take\s+all\s+(?:my\s+)?pills)\b',
    r'\b(?:can\'?t\s+cope|cannot\s+cope|can\'?t\s+go\s+on)\b',
    r'\b(?:in\s+(?:a\s+)?(?:deep\s+|severe\s+)?crisis|mental\s+health\s+crisis)\b',
    r'\b(?:everything\s+is\s+hopeless|feeling\s+hopeless)\b',
    r'\b(?:no\s+point\s+(?:in\s+)?living|better\s+off\s+dead)\b',
    r'\b(?:nobody\s+cares\s+if\s+I\s+die)\b',
]

CRISIS_REGEX = re.compile('|'.join(CRISIS_PATTERNS), re.IGNORECASE)

# Standard official signposting message taken directly from approved UCLan pages
CRISIS_SIGNPOST_MESSAGE = """### We Care About Your Safety and Wellbeing

It sounds like you are going through a very difficult time right now. As an automated assistant, **I cannot provide personal advice or therapy**, but there are compassionate, trained human professionals available right now who want to help you:

* **UCLan Mental Health & Wellbeing Service** (Mon–Fri, 9am–5pm):
  * Email: [wellbeing@uclan.ac.uk](mailto:wellbeing@uclan.ac.uk)
  * Phone: **01772 893020**
  * Location: Ground Floor, Student Centre, Preston Campus

* **24/7 On-Campus Security (Urgent / Emergency on Campus)**:
  * Phone: **01772 892068** (or call **999** for emergency services)

* **24/7 NHS Mental Health Urgent Support**:
  * Phone: **111** (Free, confidential 24-hour NHS mental health triage)

* **24/7 Free & Confidential Listening Services**:
  * **Samaritans**: Call **116 123** (free from any phone) or email [jo@samaritans.org](mailto:jo@samaritans.org)
  * **SHOUT Crisis Text Line**: Text **SHOUT** to **85258** (free 24/7 text support)
  * **Papyrus HOPELINE247** (for under-35s): Call **0800 068 4141** or text **07860 039967**

Please reach out to one of these services — you do not have to go through this alone."""


def detect_crisis(text: str) -> Tuple[bool, str, Dict[str, Any]]:
    """Inspect text for crisis or distress indicators.
    
    Returns:
        is_crisis: Boolean indicating if crisis was detected
        signpost_message: Pre-approved support contact message
        meta: Diagnostic details
    """
    if not text:
        return False, "", {}

    match = CRISIS_REGEX.search(text)
    if match:
        return True, CRISIS_SIGNPOST_MESSAGE, {
            "matched_trigger": match.group(0),
            "safety_action": "bypassed_llm_signposted_wellbeing",
            "source_url": "https://www.lancashire.ac.uk/student-life/support/mental-health-wellbeing"
        }

    return False, "", {}
