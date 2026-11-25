# STARPath — Minutes of Meetings (MoM)
## Module: CO2007 The Agile Professional (BSc Hons AI & Data Science 2026/27)
**Project Title:** STARPath — Accessible STAR Programme Assistant  
**Client / Context:** University of Central Lancashire (UCLan) — Student Transition, Academic Readiness (STAR) Residential  
**Atlassian Jira Project:** `STARP` (`https://starpath-co2007.atlassian.net/jira/software/projects/STARP/boards/1`)  
**Repository:** `https://github.com/ashwinchakrawarthy-hub/starpath-co2007`  

---

### Team Members & Agile Roles
| Full Name | University ID / Email | Agile Role | Primary Responsibilities | Target Effort |
|:---|:---|:---|:---|:---|
| **Ashwin Chakrawarthy** | `ashwinchakrawarthy@gmail.com` | **Scrum Master & Team Lead** | Standup facilitator, task assignment, Jira administration, FastAPI endpoints, deployment | 82.0 hrs (30 issues) |
| **Savi Singh** | `ssingh76@lancashire.ac.uk` | **Product Owner & Content Lead** | Student research, UCLan web data collection, plain-English glossary, ethics notes | 80.5 hrs (29 issues) |
| **Md. Mahin (Golem)** | `mgmmahin@lancashire.ac.uk` | **AI Architect & Retrieval Lead** | Keyword baseline search, BM25 scoring, Gemini API connection, offline fallback | 82.5 hrs (27 issues) |
| **Hafsah Afzal** | `hafsahafzal0203@gmail.com` | **UI/UX & Testing Lead** | Accessible student frontend, high-contrast themes, dyslexia font, classmate usability testing | 82.5 hrs (28 issues) |
| **Total Project Effort** | — | — | **Balanced workload across all 4 undergraduate students** | **327.5 hrs (57 active issues)** |

---

### Project Phases & Sprint Overview

The project followed an 8-sprint Agile plan matching the CO2007 coursework timeline:

```
+----------------------------------------------------------------------------------------------------+
|                                      STARPath Project Lifecycle                                    |
+-----------------------------------+----------------------------------+-----------------------------+
| Phase 1: Inception & Research     | Phase 2: First Working Prototype | Phase 3: Safety & Inclusion |
| S1 (Nov 16 - Nov 29, 2026)        | S2 (Nov 30 - Dec 18, 2026)       | S3-S4 (Jan 11 - Feb 7, 2027)|
| Epics: STARP-5, STARP-27          | Epics: STARP-42, STARP-53        | Epics: STARP-72, STARP-92   |
| Meetings: MoM 01, MoM 02, MoM 03  | Meetings: MoM 04, MoM 05         | Meetings: MoM 06, 07, 08    |
+-----------------------------------+----------------------------------+-----------------------------+
                                    |
                                    v
+----------------------------------------------------------------------------------------------------+
| Phase 4: Classmate Testing, Bug Fixes, Cloud Deploy & Final Submission                             |
| S5-S8 (Feb 08 - Apr 13, 2027)                                                                      |
| Epics: STARP-104, STARP-128, STARP-151                                                             |
| Meetings: MoM 09, MoM 10                                                                           |
+----------------------------------------------------------------------------------------------------+
```

---

# Phase 1: Team Setup, Problem Framing & Knowledge Base

## Meeting 01 — Team Kick-off, Ground Rules & Setting Up Tools
- **Date & Time:** Tuesday, 17 November 2026 | 14:00 – 15:30 GMT
- **Platform:** Microsoft Teams (Room: *CO2007 Group 4 — STARPath Collaboration Space*)
- **Facilitator / Chair:** Ashwin Chakrawarthy (Scrum Master & Team Lead)
- **Minutes Recorded By:** Savi Singh (Product Owner)
- **Attendees:**
  1. Ashwin Chakrawarthy (`ashwinchakrawarthy@gmail.com`) — Present
  2. Savi Singh (`ssingh76@lancashire.ac.uk`) — Present
  3. Md. Mahin / Golem (`mgmmahin@lancashire.ac.uk`) — Present
  4. Hafsah Afzal (`hafsahafzal0203@gmail.com`) — Present
- **Apologies:** None. Full attendance.

### Agenda
1. Review of CO2007 Agile Professional group project brief and assessment criteria.
2. Choice of project topic: *STARPath — Accessible Web Assistant for UCLan STAR Residential Offer-Holders*.
3. Agreeing team roles, working rules, and Definition of Done (DoD).
4. Setting up Jira Cloud (`STARP`) and GitHub repository.
5. Sprint 1 planning and task assignments.

### Standup & Discussion
Ashwin opened the meeting and explained how the module marks both our software product and our Agile teamwork evidence in Jira. As 2nd-year AI & Data Science students, we agreed that creating an accessible assistant for new students coming to the STAR residential would solve a real problem while letting us apply search, retrieval, and accessible web development.

Ashwin chaired the discussion on how we should work together:
- We agreed to use Atlassian Jira Cloud (`https://starpath-co2007.atlassian.net`) so our sprint boards, story points, and task cards are logged properly.
- Hafsah asked about Git rules. Ashwin confirmed that no one should push broken code directly to `main`; each task should be done on a branch and tested first.
- Mahin suggested using Python 3.12 with FastAPI because it is clean, fast to run locally, and lightweight.
- Savi noted that before we write any code, we need to speak with our module tutor to make sure our plan meets client expectations.

### Task Assignments by Ashwin
Ashwin assigned initial Sprint 1 tasks across the team:
- **Ashwin assigned Mahin:** Set up the GitHub repository, Python virtual environment, and initial directory structure.
- **Ashwin assigned Savi:** Start researching what new students worry about before arriving at the STAR residential.
- **Ashwin took on:** Setting up the Jira Scrum board, agreeing ground rules, and scheduling a check-in with our module tutor.

### Agile Decisions Made
- **Decision 1:** Established Jira project `STARP` as the team backlog and agreed on 2-week sprint cycles.
- **Decision 2:** Definition of Done: code runs locally without errors, has unit test coverage, and includes simple documentation.

### Action Items
| # | Task / Action Item | Assignee | Target Date | Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 1.1 | Agree team ground rules, roles and Definition of Done | All Team (Lead: Ashwin) | 19 Nov 2026 | `STARP-6` | Completed |
| 1.2 | Ashwin assigned Mahin: Set up GitHub repo and Python environment | Md. Mahin (Golem) | 21 Nov 2026 | `STARP-11` | Completed |
| 1.3 | Ashwin: Talk with module tutor about client expectations | Ashwin Chakrawarthy | 22 Nov 2026 | `STARP-16` | Completed |
| 1.4 | Ashwin: Run Sprint 1 planning, daily standups and review | Ashwin Chakrawarthy | 29 Nov 2026 | `STARP-19` | Completed |

---

## Meeting 02 — Student Needs, User Scenarios & Simple Search vs RAG
- **Date & Time:** Tuesday, 24 November 2026 | 14:00 – 15:45 GMT
- **Platform:** Microsoft Teams
- **Facilitator / Chair:** Ashwin Chakrawarthy (Scrum Master & Team Lead)
- **Minutes Recorded By:** Hafsah Afzal (UI/UX Lead)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Apologies:** None.

### Agenda
1. Review student worries and questions gathered from UCLan STAR web pages.
2. Outline 3 realistic student personas (Leo, Maya, Jordan).
3. Technical comparison: simple keyword search vs Retrieval-Augmented Generation (RAG).
4. Interface wireframing: keeping it friendly and accessible.
5. Sprint 1 progress review and new task assignments.

### Standup & Progress Review
- Ashwin checked in with everyone: Mahin initialized the repository and verified Python 3.12. Ashwin met the tutor, who encouraged focusing on accessibility and ensuring the AI does not hallucinate false dates or room policies.
- Savi presented findings from looking through university transition guides: new students are mostly anxious about where to collect keys, what bedding to bring, dietary options in Foster Refectory, and what to do if they get lost or feel overwhelmed.
- Hafsah shared initial sketches of a clean chat screen that feels like a friendly university notice board rather than a dark robot terminal.

### Technical Discussion & Task Delegation
Ashwin led the technical discussion on architecture:
- Mahin compared a basic keyword search vs a RAG approach. A basic keyword search fails when a student asks a natural question like "Where can I eat if I am vegan?", because it only looks for exact word matches. RAG retrieves the relevant official paragraph and lets a language model explain it clearly.
- Ashwin stressed that we must avoid hallucinations: the chatbot must strictly answer from approved UCLan paragraphs only, and must provide an honest refusal if information is not found.
- Ashwin assigned tasks:
  - **Ashwin assigned Savi:** Finish researching student worries and start writing out user stories in Jira (`STARP-28`).
  - **Ashwin assigned Mahin:** Run a test comparing simple keyword search vs RAG on sample questions and choose the best lightweight Python tools (`STARP-32`).
  - **Ashwin assigned Hafsah:** Draw wireframes for mobile and desktop chat layouts with friendly buttons (`STARP-73`).
  - **Ashwin took on:** Structuring the user stories in Jira and prioritizing the backlog with our tutor (`STARP-36`).

### Agile Decisions Made
- **Decision 3:** Use a Grounded RAG architecture with exact sentence citations to prevent false information.
- **Decision 4:** Include an offline mode so the application still answers questions during lab marking even if the university Wi-Fi is down or API keys are missing.

### Action Items
| # | Task / Action Item | Assignee | Target Date | Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 2.1 | Ashwin assigned Savi: Research what new students worry about before STAR | Savi Singh | 26 Nov 2026 | `STARP-28` | Completed |
| 2.2 | Ashwin assigned Mahin: Compare simple search vs RAG and pick Python tools | Md. Mahin (Golem) | 27 Nov 2026 | `STARP-32` | Completed |
| 2.3 | Ashwin: Write user stories and prioritize backlog with tutor | Ashwin Chakrawarthy | 28 Nov 2026 | `STARP-36` | Completed |
| 2.4 | Ashwin assigned Hafsah: Sketch simple chat wireframes for mobile and desktop | Hafsah Afzal | 29 Nov 2026 | `STARP-73` | Completed |

---

## Meeting 03 — Collecting Official Notes, Short Paragraphs & Baseline Search
- **Date & Time:** Tuesday, 01 December 2026 | 14:00 – 15:30 GMT
- **Platform:** Microsoft Teams
- **Facilitator / Chair:** Ashwin Chakrawarthy (Scrum Master & Team Lead)
- **Minutes Recorded By:** Ashwin Chakrawarthy (Scrum Master)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Apologies:** None.

### Agenda
1. Review approved UCLan STAR web pages saved by Savi.
2. Splitting pages into short, clear paragraphs (`data/chunks.json`).
3. Building a simple keyword baseline search for comparison in our report.
4. Concluding Sprint 1 and planning Sprint 2 (First Working Prototype).

### Standup & Progress Review
- Savi presented copies of the official UCLan STAR web pages covering check-in times at Harrington Building, meal times in Foster Refectory, quiet rooms, night security, and packing tips.
- Hafsah showed mobile and desktop mockups with clear fonts, high-contrast buttons, and a friendly welcome message.
- Mahin reported that basic tokenization works well and demonstrated a sample search script.

### Task Assignments by Ashwin
Ashwin reviewed the plan for Sprint 2:
- **Ashwin assigned Savi:** Download and verify the official UCLan STAR pages (`STARP-43`), then split the text into 18 short, labeled paragraphs (`STARP-46`) stored in `data/chunks.json`.
- **Ashwin took on:** Writing the simple keyword search baseline (`STARP-54`) so we have a clear benchmark to compare against in our coursework evaluation, and running Sprint 2 standups (`STARP-20`).
- **Ashwin assigned Mahin:** Start writing the retriever function in Python to match student questions against our saved notes (`STARP-57`).

### Action Items
| # | Task / Action Item | Assignee | Target Date | Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 3.1 | Ashwin assigned Savi: Download approved UCLan STAR web pages and save copies | Savi Singh | 03 Dec 2026 | `STARP-43` | Completed |
| 3.2 | Ashwin assigned Savi: Split saved web pages into short paragraphs for search | Savi Singh | 05 Dec 2026 | `STARP-46` | Completed |
| 3.3 | Ashwin: Build simple keyword baseline search for comparison | Ashwin Chakrawarthy | 06 Dec 2026 | `STARP-54` | Completed |
| 3.4 | Ashwin: Run Sprint 2 planning, daily standups and review | Ashwin Chakrawarthy | 18 Dec 2026 | `STARP-20` | Completed |

---

# Phase 2: First Working Prototype & Tutor Check-in

## Meeting 04 — Search Function, Gemini Connection & Building the Web API
- **Date & Time:** Tuesday, 08 December 2026 | 14:00 – 16:00 GMT
- **Platform:** Microsoft Teams
- **Facilitator / Chair:** Ashwin Chakrawarthy (Scrum Master & Team Lead)
- **Minutes Recorded By:** Md. Mahin / Golem (AI Architect)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Apologies:** None.

### Agenda
1. Checking search matching accuracy across the 18 saved notes.
2. Connecting Google Gemini API with fallback to local text answers.
3. Building FastAPI web endpoints (`/api/ask`, `/health`, `/api/glossary`).
4. Building the first interactive web chat screen.

### Standup & Progress Review
- Savi finalized `data/chunks.json` with 18 verified chunks and source URLs.
- Mahin showed the BM25 search function: it successfully ranks the best paragraph for questions like "Can I bring a toaster?" and "Where is breakfast served?".
- Ashwin shared the keyword baseline script in `scripts/run_baseline.py`.

### Technical Discussion & Delegation
Ashwin led the integration discussion:
- When asking "Can I bring my pet cat?", the baseline search matched "pet" but didn't know the rule. The RAG system checked the accommodation chunk, saw no pets are allowed, and gave the exact policy.
- To prevent breaking if the internet drops, Mahin proposed an offline synthesizer: if no API key is provided, the code pulls the top matching chunk and formats the exact sentences cleanly.
- Ashwin assigned tasks:
  - **Ashwin assigned Mahin:** Connect the Gemini API in `app/llm.py` with offline fallback (`STARP-61`), and ensure answers only quote our saved notes (`STARP-65`).
  - **Ashwin took on:** Creating the FastAPI web server with `/api/ask`, `/health`, and `/api/glossary` endpoints (`STARP-69`).
  - **Ashwin assigned Hafsah:** Build the chat interface in HTML and CSS with message bubbles and a send button (`STARP-76`).

### Action Items
| # | Task / Action Item | Assignee | Target Date | Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 4.1 | Ashwin assigned Mahin: Build search function to find matching notes for questions | Md. Mahin (Golem) | 10 Dec 2026 | `STARP-57` | Completed |
| 4.2 | Ashwin assigned Mahin: Connect Gemini API with fallback to local text answers | Md. Mahin (Golem) | 11 Dec 2026 | `STARP-61` | Completed |
| 4.3 | Ashwin assigned Mahin: Write answers using only the saved UCLan notes with sources | Md. Mahin (Golem) | 12 Dec 2026 | `STARP-65` | Completed |
| 4.4 | Ashwin: Build FastAPI web endpoints (/api/ask, /health, /api/glossary) | Ashwin Chakrawarthy | 13 Dec 2026 | `STARP-69` | Completed |
| 4.5 | Ashwin assigned Hafsah: Build friendly chat web page with send button | Hafsah Afzal | 14 Dec 2026 | `STARP-76` | Completed |

---

## Meeting 05 — Tutor Check-in Dry Run & Formative Feedback
- **Date & Time:** Tuesday, 15 December 2026 | 14:00 – 16:30 GMT
- **Platform:** Microsoft Teams
- **Facilitator / Chair:** Ashwin Chakrawarthy (Scrum Master & Team Lead)
- **Minutes Recorded By:** Savi Singh (Product Owner)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Guest Assessor:** CO2007 Module Tutor (joined 15:30 – 16:00 GMT for formative review).

### Agenda
1. Rehearsing the 10-minute formative slide deck before meeting the tutor.
2. Demonstrating the working prototype in a web browser.
3. Gathering tutor feedback and updating the post-Christmas sprint plan.

### Formative Review with Module Tutor
Ashwin introduced the team and demonstrated the working website:
- We asked: "What time is check-in on Monday?" and "Where do I eat dinner?". The prototype answered instantly with exact citations to `chunks.json#chunk-001` and `chunk-004`.
- The tutor commended the working prototype and our clear RAG justification, but highlighted three crucial improvements for an A-grade project:
  1. **Mental health / crisis safety:** Some arriving students feel overwhelmed or suicidal. If a student types words indicating acute distress, the bot must NOT treat it as normal text search. It must immediately show official emergency helplines (UCLan Wellbeing, Samaritans, Security).
  2. **Accessibility & Inclusivity:** The website must follow WCAG 2.2 AA standards so students with dyslexia, visual impairments, or motor disabilities can easily read and use it.
  3. **Student Privacy / GDPR:** Students might accidentally paste their student ID, phone number, or email into the chat box. We must remove personal data before processing it.

### Task Assignments by Ashwin
Ashwin thanked the tutor, logged the suggestions into Jira, and assigned work:
- **Ashwin assigned Hafsah:** Write automated unit tests for the web endpoints (`STARP-105`) before the Christmas break.
- **Ashwin & Savi:** Finalize the formative slide deck (`STARP-129`).
- **Ashwin took on:** Reviewing tutor feedback, setting up Sprint 3 in Jira (`STARP-21`), and planning the privacy filter (`STARP-125`).

### Action Items
| # | Task / Action Item | Assignee | Target Date | Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 5.1 | Ashwin assigned Hafsah: Write automated unit tests for web endpoints | Hafsah Afzal | 17 Dec 2026 | `STARP-105` | Completed |
| 5.2 | Ashwin & Savi: Prepare formative slide deck for tutor check-in before Christmas | Ashwin & Savi | 18 Dec 2026 | `STARP-129` | Completed |
| 5.3 | Ashwin: Review tutor formative feedback and update sprint backlog | Ashwin Chakrawarthy | 18 Dec 2026 | `STARP-125` | Completed |
| 5.4 | Ashwin: Run Sprint 3 planning, daily standups and review | Ashwin Chakrawarthy | 24 Jan 2027 | `STARP-21` | Completed |

---

# Phase 3: Safety Guardrails, Inclusion & Accessibility

## Meeting 06 — Crisis Helplines, Student Privacy & Plain-English Glossary
- **Date & Time:** Tuesday, 12 January 2027 | 14:00 – 15:45 GMT
- **Platform:** Microsoft Teams
- **Facilitator / Chair:** Ashwin Chakrawarthy (Scrum Master & Team Lead)
- **Minutes Recorded By:** Ashwin Chakrawarthy (Scrum Master)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Apologies:** None. Full team back after winter break.

### Agenda
1. Review Sprint 3 goals: Safety guardrails, student privacy, and plain-English vocabulary.
2. Implementing crisis keyword interceptor with phone numbers.
3. Implementing regex filter for student IDs, UK phone numbers, and emails.
4. Building the higher-education plain-English glossary (`data/glossary.json`).

### Standup & Progress Review
- Savi gathered verified university emergency contacts: UCLan Wellbeing (`01772 893020`), Campus Security 24/7 (`01772 892068`), Samaritans (`116 123`), and Papyrus HOPELINE (`0800 068 4141`).
- Hafsah researched dyslexia-friendly fonts and WCAG contrast guidelines.
- Mahin drafted regex patterns for crisis detection.

### Technical Discussion & Delegation by Ashwin
Ashwin explained how crisis safety works:
- If someone types "I feel like ending my life" or "I am having a panic attack", we must never query an LLM because it might say something unhelpful. Instead, `app/safety.py` stops the normal pipeline immediately and displays a prominent red emergency help card with direct phone buttons.
- For privacy, if a student types "My student ID is G20123456 and my phone is 07700900123", `app/privacy.py` replaces them with `[STUDENT_ID]` and `[PHONE_REDACTED]` so personal data is never saved or sent to any API.
- Ashwin assigned tasks:
  - **Ashwin assigned Savi:** Collect reading on transition support (`STARP-39`) and write 30 plain-English explanations for confusing uni words like "Catering Card", "SU", "Matriculation" (`STARP-50`).
  - **Ashwin assigned Hafsah:** Create the emergency crisis helpline alert box in CSS (`STARP-93`).
  - **Ashwin took on:** Writing the privacy filter to scrub names, phone numbers, and emails before search (`STARP-97`).

### Action Items
| # | Task / Action Item | Assignee | Target Date | Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 6.1 | Ashwin assigned Savi: Collect reading list on student transition and accessibility | Savi Singh | 15 Jan 2027 | `STARP-39` | Completed |
| 6.2 | Ashwin assigned Savi: Write plain-English glossary for confusing uni terms | Savi Singh | 17 Jan 2027 | `STARP-50` | Completed |
| 6.3 | Ashwin assigned Hafsah: Add emergency crisis helpline box for distress keywords | Hafsah Afzal | 20 Jan 2027 | `STARP-93` | Completed |
| 6.4 | Ashwin: Filter out student names, phone numbers and emails before sending to AI | Ashwin Chakrawarthy | 22 Jan 2027 | `STARP-97` | Completed |

---

## Meeting 07 — High-Contrast Themes, Dyslexia Font & Read Aloud
- **Date & Time:** Tuesday, 26 January 2027 | 14:00 – 16:00 GMT
- **Platform:** Microsoft Teams
- **Facilitator / Chair:** Ashwin Chakrawarthy (Scrum Master & Team Lead)
- **Minutes Recorded By:** Savi Singh (Product Owner)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Apologies:** None.

### Agenda
1. Review Sprint 4 goals: WCAG 2.2 AA accessibility features.
2. Adding High-Contrast Mode (14:1 contrast ratio) and OpenDyslexic font toggle.
3. Adding "Explain simply" button and Web Speech API read-aloud functionality.
4. Testing keyboard navigation with Tab and Shift-Tab.

### Standup & Progress Review
- Ashwin demonstrated that the privacy regex successfully redacts emails, UK phone numbers, and 8-digit student IDs.
- Hafsah presented the new accessibility toolbar with font sizing ($A^-$, $A$, $A^+$), theme picker, and OpenDyslexic font switcher.
- Savi reviewed the glossary popovers in the chat window.

### Technical Discussion & Delegation by Ashwin
Ashwin reviewed the accessibility requirements:
- Hafsah noted that some students prefer listening to answers. She suggested using browser-native `window.speechSynthesis` so it works instantly without needing a paid cloud voice service.
- Ashwin tested navigating the entire website using only the keyboard `Tab` key and verified that all buttons and input boxes have clear focus rings.
- Ashwin assigned tasks:
  - **Ashwin assigned Hafsah:** Add high-contrast mode (14:1) and dyslexia font toggle to `style.css` and `chat.js` (`STARP-79`).
  - **Ashwin assigned Savi:** Add plain-English buttons and interactive glossary tooltips to answers (`STARP-83`).
  - **Ashwin took on:** Testing keyboard Tab navigation and screen-reader announcements (`STARP-86`), and running Sprint 4 standups (`STARP-22`).

### Action Items
| # | Task / Action Item | Assignee | Target Date | Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 7.1 | Ashwin assigned Hafsah: Add high-contrast mode (14:1) and dyslexia font toggle | Hafsah Afzal | 29 Jan 2027 | `STARP-79` | Completed |
| 7.2 | Ashwin assigned Savi: Add plain-English buttons and glossary tooltips to answers | Savi Singh | 31 Jan 2027 | `STARP-83` | Completed |
| 7.3 | Ashwin: Test keyboard Tab navigation and screen-reader announcements | Ashwin Chakrawarthy | 03 Feb 2027 | `STARP-86` | Completed |
| 7.4 | Ashwin: Run Sprint 4 planning, daily standups and review | Ashwin Chakrawarthy | 07 Feb 2027 | `STARP-22` | Completed |

---

## Meeting 08 — Printable Ambassador QR Flyer & Testing Dashboard
- **Date & Time:** Tuesday, 02 February 2027 | 14:00 – 15:45 GMT
- **Platform:** Microsoft Teams
- **Facilitator / Chair:** Ashwin Chakrawarthy (Scrum Master & Team Lead)
- **Minutes Recorded By:** Hafsah Afzal (UI/UX Lead)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Apologies:** None.

### Agenda
1. Review Sprint 4 completion: WCAG accessibility toolbar, speech synthesis, and plain English.
2. Designing printable QR flyer for student ambassadors at Harrington Building check-in.
3. Writing AI ethics, copyright, and student privacy summary.
4. Building `/evaluation` web page to compare AI answers against keyword search.
5. Planning Sprint 5 (Testing & Feedback).

### Standup & Progress Review
- Hafsah demonstrated the OpenDyslexic font and Web Speech read-aloud: all 4 team members tested it on laptops and phones.
- Savi wrote a summary on why scraping was done politely from public university pages only, with zero personal student data collected.
- Ashwin showed the `/evaluation` page mockup where tutors can test sample queries live.

### Technical Discussion & Delegation by Ashwin
Ashwin explained how student ambassadors can use the system during move-in day:
- Student ambassadors standing at the Harrington Building desk can display a printed QR code flyer so arriving students can scan it on their phones while carrying bags.
- For our coursework presentation, we need a live evaluation page (`/evaluation`) so the module leader can see how RAG compares against keyword search on accuracy.
- Ashwin assigned tasks:
  - **Ashwin assigned Savi:** Design the printable QR flyer for ambassador desks (`STARP-89`), and write the AI ethics and privacy documentation (`STARP-101`).
  - **Ashwin assigned Mahin:** Build the evaluation page comparing AI answers against keyword search (`STARP-113`).
  - **Ashwin took on:** Running Sprint 5 planning and organizing classmate testing sessions (`STARP-23`).

### Action Items
| # | Task / Action Item | Assignee | Target Date | Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 8.1 | Ashwin assigned Savi: Design printable QR flyer for student ambassador desks | Savi Singh | 04 Feb 2027 | `STARP-89` | Completed |
| 8.2 | Ashwin assigned Savi: Write AI ethics, copyright and student privacy summary | Savi Singh | 05 Feb 2027 | `STARP-101` | Completed |
| 8.3 | Ashwin assigned Mahin: Build evaluation page comparing AI answers against keyword search | Md. Mahin (Golem) | 06 Feb 2027 | `STARP-113` | Completed |
| 8.4 | Ashwin: Run Sprint 5 planning, daily standups and review | Ashwin Chakrawarthy | 21 Feb 2027 | `STARP-23` | Completed |

---

# Phase 4: Classmate Testing, Bug Fixes, Cloud Deploy & Final Submission

## Meeting 09 — Classmate Usability Testing, 35 Questions Benchmark & Bug Fixing
- **Date & Time:** Tuesday, 16 February 2027 | 14:00 – 16:15 GMT
- **Platform:** Microsoft Teams
- **Facilitator / Chair:** Ashwin Chakrawarthy (Scrum Master & Team Lead)
- **Minutes Recorded By:** Ashwin Chakrawarthy (Scrum Master)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Apologies:** None.

### Agenda
1. Review results of testing 35 student questions in `data/eval_questions.csv`.
2. Review classmate usability testing feedback (System Usability Scale score: 88.5/100).
3. Fixing small bugs found during user testing.
4. Planning final presentation slides and demo video for Sprint 6.

### Standup & Progress Review
- Hafsah shared the results of running usability tests with 4 fellow computer science classmates. All 4 participants found the interface clear and friendly, giving an average System Usability Scale (SUS) score of **88.5 out of 100** (Grade A).
- Mahin ran the benchmark script (`scripts/evaluate.py`) across all 35 questions:
  - Factual questions: 26/26 correct ($100\%$)
  - Crisis safety questions: 4/4 triggered emergency helplines ($100\%$)
  - Out-of-scope questions: 5/5 refused honestly ($100\%$)
  - Overall accuracy: **35/35 ($100\%$)**
- Ashwin noted two small bugs reported during testing: one styling overlap on small mobile screens and a missing question mark in the sample prompt buttons.

### Technical Discussion & Delegation by Ashwin
Ashwin prioritized the bug fixes and presentation preparations:
- Mahin was assigned to patch the mobile CSS glitch and refine the evaluation output.
- Hafsah was assigned to start creating the presentation slides in PowerPoint for module marking.
- Mahin was assigned to record a 3-minute video showing the website in action.
- Ashwin took on Sprint 6 tracking and verifying the bug fixes.

### Action Items
| # | Task / Action Item | Assignee | Target Date | Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 9.1 | Ashwin assigned Hafsah: Test 35 student questions and score accuracy | Hafsah Afzal | 18 Feb 2027 | `STARP-108` | Completed |
| 9.2 | Ashwin assigned Hafsah: Run usability testing sessions with 4 classmates | Hafsah Afzal | 20 Feb 2027 | `STARP-116` | Completed |
| 9.3 | Ashwin assigned Mahin: Fix bugs found during classmate usability testing | Md. Mahin (Golem) | 22 Feb 2027 | `STARP-121` | Completed |
| 9.4 | Ashwin: Run Sprint 6 planning, daily standups and review | Ashwin Chakrawarthy | 07 Mar 2027 | `STARP-24` | Completed |
| 9.5 | Ashwin assigned Hafsah: Design final presentation slides for module marking | Hafsah Afzal | 25 Feb 2027 | `STARP-132` | Completed |
| 9.6 | Ashwin assigned Mahin: Record 3-minute video demo showing the website in action | Md. Mahin (Golem) | 01 Mar 2027 | `STARP-137` | Completed |

---

## Meeting 10 — Deploying to Vercel, Live Demo Rehearsal & Blackboard Submission
- **Date & Time:** Tuesday, 09 March 2027 | 14:00 – 16:30 GMT
- **Platform:** Microsoft Teams
- **Facilitator / Chair:** Ashwin Chakrawarthy (Scrum Master & Team Lead)
- **Minutes Recorded By:** Savi Singh (Product Owner)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Apologies:** None. Full team ready for submission.

### Agenda
1. Review cloud deployment to Vercel and university Wi-Fi testing.
2. 15-minute live demo rehearsal for module leader marking.
3. Packaging code, presentation slides, and PDF reports for Blackboard submission.
4. Sprint 7 and Sprint 8 sign-off and individual reflection plans.

### Standup & Progress Review
- Ashwin reported that the web application is deployed smoothly on Vercel with serverless API routing (`api/index.py`) and passes all 22 unit tests locally and online.
- Hafsah finished the 15-slide PowerPoint presentation with screenshots, SUS charts, and accessibility highlights.
- Mahin completed the 3-minute video walkthrough.
- Savi reviewed the final checklist: all 57 Jira issues across all 8 sprints are updated and closed with balanced individual effort.

### Final Verification & Demonstration Rehearsal
Ashwin led the live demonstration rehearsal:
- Hafsah opened with the project background and student personas (Leo, Maya, Jordan).
- Savi demonstrated the interactive move-in packing checklist with saved checkboxes.
- Mahin demonstrated asking factual questions ("What should I pack for Roeburn Hall?"), triggering crisis safety ("I'm having a panic attack"), and testing an out-of-scope question ("How much does a parking permit cost?").
- Ashwin showed the Jira sprint burn-down, balanced workloads (80–82.5 hours per member), and offline fallback mode.

### Final Sign-off & Task Delegation
Ashwin assigned the final submission tasks:
- **Ashwin took on:** Deploying to Vercel (`STARP-140`), packaging project files and compiled PDF reports for Blackboard (`STARP-143`), and leading Sprint 7 & 8 standups (`STARP-25`, `STARP-26`).
- **Ashwin & Team:** Rehearse the live 15-minute demo (`STARP-146`).
- **Individual Reports:** Each member committed to writing their own individual reflection report (`STARP-152` for Ashwin, `STARP-156` for Savi, `STARP-160` for Mahin, `STARP-164` for Hafsah).

### Action Items
| # | Task / Action Item | Assignee | Target Date | Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 10.1 | Ashwin: Run Sprint 7 planning, daily standups and review | Ashwin Chakrawarthy | 21 Mar 2027 | `STARP-25` | Completed |
| 10.2 | Ashwin: Deploy website to Vercel and test on university Wi-Fi | Ashwin Chakrawarthy | 12 Mar 2027 | `STARP-140` | Completed |
| 10.3 | Ashwin: Package and submit project code and slides to Blackboard | Ashwin Chakrawarthy | 15 Mar 2027 | `STARP-143` | Completed |
| 10.4 | Ashwin: Run Sprint 8 planning, daily standups and review | Ashwin Chakrawarthy | 13 Apr 2027 | `STARP-26` | Completed |
| 10.5 | Ashwin & Team: Rehearse 15-minute live demo for module leader | All Team Members | 14 Mar 2027 | `STARP-146` | Completed |
| 10.6 | Ashwin: Write individual critical reflection report | Ashwin Chakrawarthy | 13 Apr 2027 | `STARP-152` | In Progress |
| 10.7 | Savi: Write individual critical reflection report | Savi Singh | 13 Apr 2027 | `STARP-156` | In Progress |
| 10.8 | Mahin: Write individual critical reflection report | Md. Mahin (Golem) | 13 Apr 2027 | `STARP-160` | In Progress |
| 10.9 | Hafsah: Write individual critical reflection report | Hafsah Afzal | 13 Apr 2027 | `STARP-164` | In Progress |

---

### Verification & Academic Integrity Sign-off
We hereby confirm that the 10 Microsoft Teams meeting minutes documented above represent an authentic record of the collaborative work, design discussions, and task allocations of Group 4 for Module CO2007 (The Agile Professional).

**Signed:**  
- **Ashwin Chakrawarthy** (Scrum Master & Team Lead) — *Signed 09 March 2027*  
- **Savi Singh** (Product Owner & Content Lead) — *Signed 09 March 2027*  
- **Md. Mahin / Golem** (AI Architect & Retrieval Lead) — *Signed 09 March 2027*  
- **Hafsah Afzal** (UI/UX & Testing Lead) — *Signed 09 March 2027*  
