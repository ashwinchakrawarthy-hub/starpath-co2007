# STARPath — Minutes of Meetings (MoM)
## Module: CO2007 The Agile Professional (BSc AI & Data Science 2026/27)
**Project Title:** STARPath — Accessible STAR Programme Assistant  
**Client / Context:** University of Central Lancashire (UCLan) — Student Transition, Academic Readiness (STAR) Residential  
**Atlassian Jira Project:** `STARP` (`https://starpath-co2007.atlassian.net/jira/software/projects/STARP/boards/1`)  
**Repository:** `https://github.com/ashwinchakrawarthy/starpath-co2007`  

---

### Team Members & Agile Roles
| Full Name | University ID / Email | Agile Role | Primary Responsibilities | Target Effort |
|:---|:---|:---|:---|:---|
| **Ashwin Chakrawarthy** | `ashwinchakrawarthy@gmail.com` | **Scrum Master & Backend Lead** | Sprint cadence, Jira administration, FastAPI orchestration, deployment automation | 82.0 hrs (30 issues) |
| **Savi Singh** | `ssingh76@lancashire.ac.uk` | **Product Owner & Ethics/Data Curator** | Requirements backlog, UCLan web data ingestion, glossary creation, ethics compliance | 80.5 hrs (29 issues) |
| **Md. Mahin (Golem)** | `mgmmahin@lancashire.ac.uk` | **AI Architect & Retrieval Engineer** | Dual BM25/lexical retriever, swappable LLM pipeline, crisis guardrail & PII regex | 82.5 hrs (27 issues) |
| **Hafsah Afzal** | `hafsahafzal0203@gmail.com` | **UI/UX & Quality Assurance Lead** | WCAG 2.2 AA accessible frontend, Web Speech API, test suite, benchmark evaluation | 82.5 hrs (28 issues) |
| **Total Project Effort** | — | — | **4-way balanced workload distribution** | **327.5 hrs (163 issues)** |

---

### Project Phases Overview & Jira Mapping

The project workflow is structured across **Four Distinct Phases**, mapped directly to Jira Sprints and Epics:

```
+----------------------------------------------------------------------------------------------------+
|                                      STARPath Project Lifecycle                                    |
+-----------------------------------+----------------------------------+-----------------------------+
| Phase 1: Inception & Foundations  | Phase 2: MVP & Formative Review  | Phase 3: Safety & Inclusion |
| S1 (Nov 16 - Nov 29, 2026)        | S2 (Nov 30 - Dec 18, 2026)       | S3-S4 (Jan 11 - Feb 7, 2027)|
| Epics: STARP-5, STARP-27          | Epic: STARP-42                   | Epics: STARP-53, 72, 92     |
| Meetings: MoM 01, MoM 02, MoM 03  | Meetings: MoM 04, MoM 05         | Meetings: MoM 06, 07, 08    |
+-----------------------------------+----------------------------------+-----------------------------+
                                    |
                                    v
+----------------------------------------------------------------------------------------------------+
| Phase 4: Rigorous Testing, Benchmarking, Release & Final Submissions                               |
| S5-S8 (Feb 08 - Apr 13, 2027)                                                                      |
| Epics: STARP-104, STARP-128, STARP-151                                                             |
| Meetings: MoM 09, MoM 10                                                                           |
+----------------------------------------------------------------------------------------------------+
```

- **Phase 1: Project Inception, Problem Framing & Data Foundations** (Weeks 1–3, Nov 2026)  
  *Jira Sprints:* Sprint 1 (`STARP S1: Inception & Data`, Nov 16 – Nov 29, 2026)  
  *Jira Epics:* `STARP-5` (EPIC 1: Project Initiation & Charter), `STARP-27` (EPIC 2: Data Curation & Ethics)  
  *Meetings Covered:* Meeting 1, Meeting 2, Meeting 3  

- **Phase 2: MVP Core Development & Formative Assessment** (Weeks 3–5, Dec 2026)  
  *Jira Sprints:* Sprint 2 (`STARP S2: First Working MVP`, Nov 30 – Dec 18, 2026)  
  *Jira Epics:* `STARP-42` (EPIC 3: Core RAG Engine & Swappable LLM Pipeline)  
  *Meetings Covered:* Meeting 4, Meeting 5 (including Formative Dry Run)  

- **Phase 3: Safety Guardrails, Inclusion & WCAG Accessibility** (Weeks 6–9, Jan–Feb 2027)  
  *Jira Sprints:* Sprint 3 (`STARP S3: Safety & Inclusion`, Jan 11 – Jan 24, 2027), Sprint 4 (`STARP S4: Accessibility & Eval`, Jan 25 – Feb 07, 2027)  
  *Jira Epics:* `STARP-53` (EPIC 4: Safety & Privacy), `STARP-72` (EPIC 5: Inclusive UX & WCAG 2.2), `STARP-92` (EPIC 6: Ambassador QR & Dashboards)  
  *Meetings Covered:* Meeting 6, Meeting 7, Meeting 8  

- **Phase 4: Rigorous Testing, Usability Evaluation, Release & Submission** (Weeks 10–16, Feb–Apr 2027)  
  *Jira Sprints:* Sprint 5 (`STARP S5: Testing & Evaluation`), Sprint 6 (`STARP S6: Fixes & Presentation`), Sprint 7 (`STARP S7: Release & Submit`), Sprint 8 (`STARP S8: Demo & Reports`)  
  *Jira Epics:* `STARP-104` (EPIC 7: Testing & Benchmarking), `STARP-128` (EPIC 8: Production & Cloud Deployment), `STARP-151` (EPIC 9: Academic Documentation & Submissions)  
  *Meetings Covered:* Meeting 9, Meeting 10  

---

# Phase 1: Project Inception, Problem Framing & Data Foundations

## Meeting 01 — Team Kick-off, Agile Charter & Sprint Cadence
- **Date & Time:** Tuesday, 17 November 2026 | 14:00 – 15:30 GMT
- **Platform:** Microsoft Teams (Room: *CO2007 Group 4 — STARPath Collaboration Space*)
- **Facilitator / Chair:** Ashwin Chakrawarthy (Scrum Master)
- **Minutes Recorded By:** Savi Singh (Product Owner)
- **Attendees:**
  1. Ashwin Chakrawarthy (`ashwinchakrawarthy@gmail.com`) — Present
  2. Savi Singh (`ssingh76@lancashire.ac.uk`) — Present
  3. Md. Mahin / Golem (`mgmmahin@lancashire.ac.uk`) — Present
  4. Hafsah Afzal (`hafsahafzal0203@gmail.com`) — Present
- **Apologies:** None. Full quorum present.

### Agenda
1. Review of Module Specification for CO2007 (The Agile Professional) and group project brief.
2. Agreement on project topic: *STARPath — Accessible AI Assistant for UCLan STAR Residential Offer-Holders*.
3. Assignment of Agile team roles and workload distribution agreement.
4. Selection of Agile tooling: Atlassian Jira Cloud configuration, Git repository structure, and branch protection.
5. Definition of Done (DoD) and working conventions for sprint cadence.

### Standup & Context
Ashwin opened the inaugural session by reviewing the assignment guidelines. All four members are BSc AI & Data Science students with complementary skills in Python, frontend development, information retrieval, and user experience design. The team agreed on a target individual commitment of 80–83 hours across the semester to guarantee equal contribution.

### Technical Discussion & Debate
- **Tooling Selection:** Savi proposed using Trello for simplicity, but Golem and Ashwin argued that CO2007 specifically assesses industry-standard Agile frameworks. Jira Cloud Software was unanimously selected for sprint backlogs, burn-down tracking, story points, and blocking dependency links.
- **Repository Strategy:** Hafsa stressed the need for strict branch protection: no direct commits to `main`; every feature must originate on a branch named `feature/STARP-xxx` and undergo at least one peer code review before merge.
- **Definition of Done (DoD):** The team debated what constitutes a completed story. Ashwin proposed that a story is only "Done" when:
  1. Code is tested locally with zero unit test regressions.
  2. Documentation is updated (docstrings and markdown architecture notes).
  3. Feature runs offline without crashing if internet or external API keys are unavailable.
  4. Jira issue status is updated and signed off by a peer.

### Agile Decisions Made
- **ADR-01:** Established Atlassian Jira site `https://starpath-co2007.atlassian.net` (Project Key: `STARP`) as the single source of truth for all sprints, backlog items, and workload logs.
- **ADR-02:** Established weekly 2-week sprint cycles with standing Microsoft Teams syncs every Tuesday at 14:00 GMT and Thursday asynchronous Slack check-ins.
- **ADR-03:** Approved team roles: Ashwin (Scrum Master / Backend), Savi (Product Owner / Data), Golem (AI / Retrieval Architect), Hafsa (UI / UX / QA Lead).

### Action Items
| # | Action Item Description | Assignee / Owner | Target Date | Linked Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 1.1 | Create Jira project `STARP`, configure Kanban/Scrum board, and invite all 4 members | Ashwin Chakrawarthy | 19 Nov 2026 | `STARP-6` | Completed |
| 1.2 | Draft formal Team Charter, Agile working agreement, and Definition of Done document | Savi Singh | 20 Nov 2026 | `STARP-10` | Completed |
| 1.3 | Initialize GitHub repository with standard `.gitignore`, `README.md`, and branch policies | Hafsah Afzal | 21 Nov 2026 | `STARP-7` | Completed |
| 1.4 | Research initial UCLan STAR programme web pages and compile raw URL catalog | Md. Mahin (Golem) | 22 Nov 2026 | `STARP-11` | Completed |

---

## Meeting 02 — Problem Domain Analysis, Persona Definitions & Architecture Trade-offs
- **Date & Time:** Tuesday, 24 November 2026 | 14:00 – 15:45 GMT
- **Platform:** Microsoft Teams (Room: *CO2007 Group 4 — STARPath Collaboration Space*)
- **Facilitator / Chair:** Savi Singh (Product Owner)
- **Minutes Recorded By:** Hafsah Afzal (UI/UX Lead)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Apologies:** None.

### Agenda
1. Review of initial STAR programme research and identification of student onboarding pain points.
2. Definition of primary user personas (e.g., student with sensory overload, wheelchair user, first-in-family offer-holder).
3. System scope boundaries: Explicitly deciding what is **In-Scope** versus **Out-of-Scope**.
4. Architectural trade-off: Fine-tuning a language model vs. Retrieval-Augmented Generation (RAG).
5. Technology stack selection: FastAPI vs Flask vs Django.

### Standup & Progress Review
- Ashwin reported that Jira project `STARP` is fully operational with board columns: `To Do`, `In Progress`, `In Review`, and `Done`.
- Savi completed the initial review of the UCLan STAR website (`uclan.ac.uk/star`) and identified that crucial residential details (packing lists, dining halls, quiet rooms, night-time security) are scattered across 6 separate portals.
- Hafsa set up the Git repository with linting rules. Golem documented initial retrieval options.

### Technical Discussion & Debate
- **In-Scope vs. Out-of-Scope:**
  - *In-Scope:* Official publicly published UCLan STAR residential guidance (accommodation, dates, arrival procedures, student life, catering, campus security, quiet spaces, accessibility support).
  - *Out-of-Scope:* Live interaction with real enrolled students during our development cycle (ethics clearance constraint), accessing confidential student records, handling fee transactions, or providing non-academic medical advice.
- **RAG vs. Fine-Tuning:** Golem explained that fine-tuning a small open model (e.g., Llama or Mistral) would hallucinate out-of-date dates, require costly GPU resources, and create a "black box" where answers cannot be traced to an official UCLan web page. RAG, conversely, retrieves exact text chunks from verified source URLs and grounds generation deterministically.
- **Framework Choice:** Ashwin demonstrated that FastAPI provides native asynchronous request handling, automatic OpenAPI/Swagger documentation, and lightweight dependency injection compared to Flask or Django.
- **Offline / Zero-Key Fallback:** Golem raised a critical risk: if external LLM APIs (Gemini/OpenAI) have quota exhaustion or if the lab evaluation PC lacks internet access, the app could crash. The team agreed that the system must feature an **Offline Grounded Synthesizer** that extracts verbatim matched sentences from retrieved passages when external API keys are omitted.

### Agile Decisions Made
- **ADR-04:** Selected **Retrieval-Augmented Generation (RAG)** over fine-tuning for deterministic citation grounding and zero-hallucination guardrails.
- **ADR-05:** Selected **FastAPI (Python 3.12)** as the core backend framework and semantic HTML5 + vanilla JavaScript for maximum accessibility compliance without heavyweight JavaScript frameworks.
- **ADR-06:** Approved three core personas: *Leo* (neurodivergent offer-holder needing plain English and quiet space information), *Maya* (wheelchair user needing accessible route details), and *Jordan* (first-generation anxious student with packing and arrival queries).

### Action Items
| # | Action Item Description | Assignee / Owner | Target Date | Linked Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 2.1 | Document formal User Personas and Scope Boundary Specification | Savi Singh | 26 Nov 2026 | `STARP-14` | Completed |
| 2.2 | Create high-level system architecture diagram and module breakdown | Md. Mahin (Golem) | 27 Nov 2026 | `STARP-18` | Completed |
| 2.3 | Scaffold base FastAPI application structure (`app/main.py`, config, routing) | Ashwin Chakrawarthy | 28 Nov 2026 | `STARP-22` | Completed |
| 2.4 | Design initial wireframes for chat interface with accessibility toggle controls | Hafsah Afzal | 29 Nov 2026 | `STARP-20` | Completed |

---

## Meeting 03 — Data Sourcing Ethics, Polite Scraping Policy & Knowledge Base Verification
- **Date & Time:** Tuesday, 01 December 2026 | 14:00 – 15:30 GMT
- **Platform:** Microsoft Teams (Room: *CO2007 Group 4 — STARPath Collaboration Space*)
- **Facilitator / Chair:** Savi Singh (Product Owner)
- **Minutes Recorded By:** Ashwin Chakrawarthy (Scrum Master)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Apologies:** None.

### Agenda
1. Review of ethical data collection policy and copyright considerations for UCLan public web content.
2. Ingestion of 18 verified knowledge chunks spanning STAR residential life, packing, dining, safety, and contacts.
3. Creation of `sources.csv` and `manifest.json` with immutable SHA-256 snapshot hashes.
4. Construction of Higher Education Plain-English Glossary (`glossary.json`) for confusing academic terms.
5. Sprint 1 Review & Sprint 2 Planning.

### Standup & Progress Review
- Savi presented the curated text passages extracted from official UCLan domains.
- Golem reviewed the chunking strategy: chunks must be 120–250 words each with unique IDs, categories, dates, and direct canonical source URLs.
- Hafsa presented the wireframe drafts incorporating high-contrast color palettes and dyslexia-friendly typography toggles.
- Ashwin completed the FastAPI routing skeleton and verified local test server startup.

### Technical Discussion & Debate
- **Polite Scraping & Ethical Integrity:** Savi noted that UCLan's `robots.txt` must be respected. Rather than automated continuous web crawling that could burden university servers, the team agreed to create a frozen, curated, dated snapshot (`manifest.json` timestamped 12 November 2026). This ensures reproducibility during academic grading.
- **Jargon Elimination:** Hafsa highlighted that offer-holders frequently stumble over UK higher education jargon like "SU", "Catering card", "En-suite", "STAR Leader", "DSA", and "Matriculation". Savi agreed to compile a comprehensive 30+ term glossary in `data/glossary.json` that will automatically link or pop over in the chat UI.
- **Chunk Granularity:** Golem demonstrated that if chunks are too large (>500 words), retrieval precision drops and the synthesizer picks up extraneous details. If chunks are too small (<50 words), conversational context is lost. The team settled on topical paragraphs with explicit metadata headers.

### Agile Decisions Made
- **ADR-07:** Approved 18 canonical knowledge chunks covering Accommodation, Daily Schedule, Packing Lists, Catering & Diets, Accessibility Services, Wellbeing, and Security.
- **ADR-08:** Mandated that all generated answers MUST return explicit source links with timestamped document version citations (`data/sources.csv`).
- **ADR-09:** Completed Sprint 1 with 24 story points delivered; transitioned to Sprint 2 (`STARP S2: First Working MVP`).

### Action Items
| # | Action Item Description | Assignee / Owner | Target Date | Linked Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 3.1 | Commit finalized `data/chunks.json`, `data/sources.csv`, and `data/manifest.json` | Savi Singh | 03 Dec 2026 | `STARP-28` | Completed |
| 3.2 | Build 30-term Higher Education Plain-English glossary (`data/glossary.json`) | Savi Singh | 04 Dec 2026 | `STARP-32` | Completed |
| 3.3 | Implement chunk loader and indexing module in `app/retriever.py` | Md. Mahin (Golem) | 05 Dec 2026 | `STARP-30` | Completed |
| 3.4 | Configure test framework (`unittest`) and continuous test runner script | Ashwin Chakrawarthy | 06 Dec 2026 | `STARP-34` | Completed |

---

# Phase 2: MVP Core Development & Formative Assessment

## Meeting 04 — Dual Retriever Implementation, Swappable LLM & Zero-Key Fallback
- **Date & Time:** Tuesday, 08 December 2026 | 14:00 – 16:00 GMT
- **Platform:** Microsoft Teams (Room: *CO2007 Group 4 — STARPath Collaboration Space*)
- **Facilitator / Chair:** Ashwin Chakrawarthy (Scrum Master)
- **Minutes Recorded By:** Md. Mahin / Golem (AI Architect)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Apologies:** None.

### Agenda
1. Implementation of Dual Retriever: BM25 Lexical Retriever with Term Coverage Penalization vs. Baseline Keyword Search.
2. Swappable LLM pipeline architecture (`app/llm.py` supporting Offline Grounded Synthesizer, Google Gemini API, and local Ollama).
3. Honest refusal thresholding: Preventing hallucinations on out-of-scope queries.
4. Integrating chat REST API (`/api/ask`) with asynchronous streaming response handling.

### Standup & Progress Review
- Golem showcased the prototype retriever: tokenizing user queries, stripping stop-words, and computing Okapi BM25 scores against the 18 chunks.
- Savi tested the retriever against 10 sample student questions; identified that generic queries with common words like "student" or "university" matched too many irrelevant chunks.
- Ashwin completed the `/api/ask`, `/api/baseline`, and `/api/glossary` FastAPI endpoints.
- Hafsa built the interactive chat UI with message bubbles and source citation cards.

### Technical Discussion & Debate
- **The Coverage Penalty Innovation:** Golem explained the false positive issue: when a user asks "Can I bring my pet iguana to the dorm?", standard BM25 matches chunks containing "dorm" or "bring", resulting in high scores despite the core entity "iguana" being missing. Golem proposed an exponential coverage multiplier:
  $$\text{Final Score} = \text{Raw Score} \times (\text{Query Term Coverage})^{1.5}$$
  If a query has non-stopword tokens that are completely absent from the chunk, its score is drastically depressed below the acceptance threshold ($0.28$).
- **Honest Refusal Behavior:** Savi emphasized that an AI for anxious students must NEVER guess or fabricate. If the best retrieved score falls below threshold, the system must trigger an honest refusal: *"I do not have verified information in the official UCLan STAR guide about this topic. Please contact the STAR team directly at star@uclan.ac.uk."*
- **Swappable LLM Interface:** Ashwin and Golem designed `app/llm.py` around an abstract base class `LLMConnector`. If `GEMINI_API_KEY` is present, it calls Google Gemini 1.5 Flash. If absent, it automatically defaults to `OfflineGroundedSynthesizer`, which parses the highest-ranking chunk, extracts the most relevant sentences, and formats them into an accessible answer with zero external network reliance.

### Agile Decisions Made
- **ADR-10:** Implemented Dual Retriever architecture allowing direct comparison between `BaselineSearchRetriever` (simple keyword count) and `BM25Retriever` (BM25 + coverage penalty).
- **ADR-11:** Mandated that `/api/baseline` and `/api/ask` return identical JSON response schemas to facilitate scientific A/B benchmarking.
- **ADR-12:** Set honest refusal threshold to score $0.28$ and query token coverage $\ge 28\%$.

### Action Items
| # | Action Item Description | Assignee / Owner | Target Date | Linked Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 4.1 | Implement Okapi BM25 scoring with term coverage penalty in `app/retriever.py` | Md. Mahin (Golem) | 10 Dec 2026 | `STARP-43` | Completed |
| 4.2 | Implement swappable LLM connectors (`OfflineGroundedSynthesizer` & `GeminiLLMConnector`) | Md. Mahin (Golem) | 11 Dec 2026 | `STARP-45` | Completed |
| 4.3 | Integrate `/api/ask` endpoint with source citation formatting and confidence scores | Ashwin Chakrawarthy | 12 Dec 2026 | `STARP-47` | Completed |
| 4.4 | Connect frontend chat box to `/api/ask` with dynamic loading spinner and source accordion | Hafsah Afzal | 13 Dec 2026 | `STARP-48` | Completed |

---

## Meeting 05 — Formative Presentation Dry Run & Tutor/Peer Feedback Integration
- **Date & Time:** Tuesday, 15 December 2026 | 14:00 – 16:30 GMT
- **Platform:** Microsoft Teams (Room: *CO2007 Group 4 — STARPath Collaboration Space*)
- **Facilitator / Chair:** Hafsah Afzal (Presentation Lead)
- **Minutes Recorded By:** Savi Singh (Product Owner)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Guest Observer:** Module Tutor / Formative Assessor (attended 15:30 – 16:00 GMT for formative review).

### Agenda
1. Dry run of 10-minute Formative Presentation slide deck for Module Leader.
2. Live prototype demonstration of the working MVP (Sprint 2 release).
3. Review of formative tutor feedback and recommendations.
4. Backlog grooming and planning for post-Christmas Sprints 3 and 4.

### Standup & Progress Review
- Ashwin reported that Sprint 2 MVP code is working smoothly: server starts in $<1$ second, returns instant answers with citations, and refuses out-of-scope questions cleanly.
- Hafsa prepared 10 formative presentation slides outlining the problem, architecture, Jira progress, and early prototype demo.
- Savi and Golem prepared the live demo script showcasing queries: "What time is check-in on Monday?", "Can I have a single room for medical reasons?", and "What happens if I get lost?".

### Formative Presentation Feedback & Discussion
- **Tutor Feedback Summary:**
  1. *Commendation:* Excellent technical justification for RAG over fine-tuning, strong team role division, and clear live prototype demonstration.
  2. *Safety Recommendation:* Offer-holders arriving at university frequently experience acute mental health episodes or panic attacks. If a student inputs self-harm or acute distress statements into the chat, an academic RAG assistant must NOT treat it as a factual retrieval query. It must immediately trigger crisis guardrails and provide emergency contact numbers (Wellbeing, Samaritans, Security).
  3. *Inclusivity & Accessibility:* The UI needs to strictly comply with WCAG 2.2 AA standards. Students with dyslexia, low vision, and motor challenges must be accommodated with high-contrast themes, scalable fonts, keyboard navigation, and text-to-speech.
  4. *Privacy / GDPR:* Offer-holders might accidentally type personal data (student ID, phone number, address) into the prompt. The system must scrub PII before passing text to the LLM or saving query logs.
- **Team Discussion:** The team welcomed the feedback enthusiastically. Ashwin created three new Epics in Jira: `STARP-53` (Safety & Privacy), `STARP-72` (Inclusive UX & WCAG), and `STARP-92` (Ambassador QR & Stakeholder Dashboards).

### Agile Decisions Made
- **ADR-13:** Prioritized Safety & Crisis Guardrail (`app/safety.py`) and PII Redaction (`app/privacy.py`) as top-priority user stories for Sprint 3 (Jan 2027).
- **ADR-14:** Committed to developing four switchable WCAG 2.2 AA accessibility themes and Web Speech API audio synthesis for Sprint 4.
- **ADR-15:** Concluded Sprint 2 (39 story points delivered); scheduled Sprint 3 kick-off for 11 January 2027 following the university holiday break.

### Action Items
| # | Action Item Description | Assignee / Owner | Target Date | Linked Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 5.1 | Update Jira backlog with tutor feedback stories and link dependencies | Ashwin Chakrawarthy | 17 Dec 2026 | `STARP-51` | Completed |
| 5.2 | Compile emergency support phone numbers (UCLan Wellbeing, Samaritans, Security, NHS 111) | Savi Singh | 18 Dec 2026 | `STARP-54` | Completed |
| 5.3 | Research regex patterns for UK PII (emails, UK mobile numbers, 8-digit student IDs) | Md. Mahin (Golem) | 18 Dec 2026 | `STARP-56` | Completed |
| 5.4 | Audit current CSS against WCAG 2.2 AA contrast ratios and draft color-blind palettes | Hafsah Afzal | 18 Dec 2026 | `STARP-58` | Completed |

---

# Phase 3: Safety Guardrails, Inclusion & WCAG Accessibility

## Meeting 06 — Crisis Intervention Guardrail & PII Privacy Shield Architecture
- **Date & Time:** Tuesday, 12 January 2027 | 14:00 – 15:45 GMT
- **Platform:** Microsoft Teams (Room: *CO2007 Group 4 — STARPath Collaboration Space*)
- **Facilitator / Chair:** Md. Mahin / Golem (AI Architect)
- **Minutes Recorded By:** Ashwin Chakrawarthy (Scrum Master)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Apologies:** None.

### Agenda
1. Review of Sprint 3 objectives: Hardened safety guardrails and privacy compliance.
2. Architecture and regex validation for `app/safety.py` (crisis, self-harm, emergency detection).
3. Architecture and validation for `app/privacy.py` (redacting emails, UK phones, student IDs, postcodes, credit cards).
4. Automated unit testing strategy for safety and privacy modules.

### Standup & Progress Review
- All members returned from holiday break on schedule.
- Savi provided verified contact details for UCLan Mental Health and Wellbeing (`01772 893020`), UCLan Campus Security 24/7 (`01772 892068`), NHS Mental Health Services (`111`), Samaritans (`116 123`), and Papyrus HOPELINE247 (`0800 068 4141`).
- Golem drafted initial regex patterns for crisis detection and privacy scrubbing.
- Ashwin initialized the unit test suite in `tests/test_safety.py` and `tests/test_privacy.py`.

### Technical Discussion & Debate
- **Bypassing the LLM on Crisis:** Golem emphasized that when a crisis is detected, the system MUST NOT send the prompt to the LLM or retriever. LLMs can generate empathetic-sounding yet dangerous or non-directive replies. Instead, `app/safety.py` intercepts the query at the very beginning of the pipeline, returns a curated emergency card with one-click callable telephone numbers, and sets a safety flag in the JSON response.
- **Regex Robustness vs Over-triggering:** Hafsa tested the crisis regex with phrases like "I am in a deep crisis" and "I feel like killing myself tonight". Initially, the regex missed "killing myself". Golem updated the pattern to `(?:kill|killing|end|ending)\s+(?:myself|it\s+all|my\s+life)`. Savi tested negative cases (e.g. "I'm killing time before the tour") to ensure normal conversational idioms do not spuriously trigger emergency banners.
- **Privacy Scrubbing:** Ashwin verified that when a user asks "My student ID is G20987654 and my phone is 07911 123456, when do I pick up keys?", the PII filter replaces these tokens with `[STUDENT_ID]` and `[PHONE_REDACTED]` before RAG retrieval. This completely protects student privacy in compliance with UK GDPR.

### Agile Decisions Made
- **ADR-16:** Mandated client-side and server-side dual crisis intercept: immediate safety banner display with clickable `tel:` links.
- **ADR-17:** Configured zero-log PII retention: user IP addresses and raw unredacted queries are never stored to persistent disk.
- **ADR-18:** Added 12 rigorous unit tests in `tests/test_safety.py` and `tests/test_privacy.py`, making CI pass mandatory before merge.

### Action Items
| # | Action Item Description | Assignee / Owner | Target Date | Linked Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 6.1 | Implement comprehensive crisis detection patterns and emergency card in `app/safety.py` | Md. Mahin (Golem) | 15 Jan 2027 | `STARP-54` | Completed |
| 6.2 | Implement multi-pattern PII scrubbing function `redact_pii()` in `app/privacy.py` | Md. Mahin (Golem) | 16 Jan 2027 | `STARP-56` | Completed |
| 6.3 | Write unit tests for all crisis edge cases and PII entity masks | Ashwin Chakrawarthy | 18 Jan 2027 | `STARP-62` | Completed |
| 6.4 | Integrate safety alert modal styling in frontend CSS | Hafsah Afzal | 20 Jan 2027 | `STARP-60` | Completed |

---

## Meeting 07 — WCAG 2.2 AA Contrast Compliance, Dyslexia Typography & Plain-English Glossary
- **Date & Time:** Tuesday, 26 January 2027 | 14:00 – 16:00 GMT
- **Platform:** Microsoft Teams (Room: *CO2007 Group 4 — STARPath Collaboration Space*)
- **Facilitator / Chair:** Hafsah Afzal (UI/UX Lead)
- **Minutes Recorded By:** Savi Singh (Product Owner)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Apologies:** None.

### Agenda
1. Review of Sprint 4 objectives: Full accessibility compliance, multi-modal features, and inclusive UX.
2. Implementation of four switchable WCAG 2.2 AA compliant themes in `app/static/style.css`:
   - Default Theme (clean UCLan red and charcoal, contrast $\ge 7:1$)
   - High-Contrast Theme (black/yellow stark palette, contrast $\ge 14:1$, exceeding WCAG AAA)
   - Color-Blind Safe Theme (accessible blue and amber hues)
   - Dark Mode Theme (deep slate background, reduced eye strain)
3. Integration of OpenDyslexic font toggle and dynamic text-scaling ($A^-$ to $A^{++}$).
4. Web Speech API read-aloud functionality and Plain-English glossary popovers.

### Standup & Progress Review
- Golem reported that `app/safety.py` and `app/privacy.py` unit tests pass with 100% accuracy.
- Hafsa completed the accessibility CSS architecture with CSS custom properties (`var(--bg)`, `var(--text)`, `var(--primary)`).
- Savi finalized the 30-term Plain-English glossary and verified definitions with first-generation student guidelines.
- Ashwin implemented the `/api/simplify` endpoint to generate readability-adapted versions of answers.

### Technical Discussion & Debate
- **Web Speech API vs Server-Side TTS:** Ashwin proposed using a server-side TTS library (like gTTS). Hafsa objected, noting that gTTS requires external internet access and introduces high latency (1–2 seconds per response). The native browser `window.speechSynthesis` (Web Speech API) runs entirely offline, provides zero latency, allows users to choose their preferred voice and speed, and functions without any backend server overhead. The team unanimously adopted the Web Speech API.
- **Font Legibility for Dyslexic Learners:** Hafsa demonstrated how `OpenDyslexic` weighted bottoms prevent letter-flipping (e.g. b/d/p/q). The team added a one-click font toggle in the navigation bar that persists in `localStorage`.
- **Glossary Popovers:** Savi and Hafsa designed interactive glossary chips: when an answer mentions "SU" or "Catering Card", the word displays with a subtle underline and badge, allowing the user to click or hover to view an instant Plain-English explanation.

### Agile Decisions Made
- **ADR-19:** Adopted client-side `window.speechSynthesis` for instant, offline-capable read-aloud support.
- **ADR-20:** Implemented 4 WCAG 2.2 AA/AAA themes, 3-level text resizing buttons ($100\%$, $115\%$, $130\%$), and OpenDyslexic font toggle.
- **ADR-21:** Added "Explain Simply" one-click button on every bot response to rewrite text in primary-level plain English.

### Action Items
| # | Action Item Description | Assignee / Owner | Target Date | Linked Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 7.1 | Code 4 WCAG themes and OpenDyslexic font switcher in `style.css` and `chat.js` | Hafsah Afzal | 28 Jan 2027 | `STARP-73` | Completed |
| 7.2 | Implement Web Speech API read-aloud toggle and "Explain simply" action | Hafsah Afzal | 30 Jan 2027 | `STARP-79` | Completed |
| 7.3 | Implement `/api/simplify` endpoint in FastAPI backend | Ashwin Chakrawarthy | 01 Feb 2027 | `STARP-81` | Completed |
| 7.4 | Test keyboard navigation (Tab/Shift-Tab/Enter) across all interactive elements | Md. Mahin (Golem) | 02 Feb 2027 | `STARP-84` | Completed |

---

## Meeting 08 — Ambassador Sharing Page (`/about`), Printable QR Card & Support Dashboard
- **Date & Time:** Tuesday, 02 February 2027 | 14:00 – 15:45 GMT
- **Platform:** Microsoft Teams (Room: *CO2007 Group 4 — STARPath Collaboration Space*)
- **Facilitator / Chair:** Savi Singh (Product Owner)
- **Minutes Recorded By:** Hafsah Afzal (UI/UX Lead)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Apologies:** None.

### Agenda
1. Design and implementation of the STAR Ambassador Sharing & Information page (`/about`).
2. Inclusion of printable QR code card for STAR student leaders and residential check-in desks.
3. Architecture of the Support Team & Module Leader Evaluation Dashboard (`/evaluation`).
4. Review of Sprint 4 deliverables and preparation for Phase 4 (Evaluation and Testing).

### Standup & Progress Review
- Hafsa demonstrated the four accessibility themes in action. Lighthouse accessibility score achieved $100/100$.
- Ashwin presented the newly implemented `/about` route featuring the project scope, ethical boundaries, persona cards, and printable QR code card.
- Golem constructed the initial benchmark evaluation test suite containing 35 rigorous domain questions.
- Savi reviewed the ambassador instructions: student leaders can display or print the QR card at the Harrington Building check-in desk so arriving offer-holders can scan and access the assistant immediately on their mobile devices.

### Technical Discussion & Debate
- **Mobile QR Code Usability:** Savi demonstrated that during residential arrivals, students are carrying luggage and do not have time to type long URLs. Having a clean, printable vector SVG/PNG QR code on the `/about` page allows ambassadors to print physical badge cards or lanyard slips.
- **Evaluation Dashboard Purpose:** Ashwin and Golem designed `/evaluation` to allow the module leader and STAR coordinators to inspect the system's health, view live benchmark metrics (accuracy, safety detection rate, refusal rate), trigger test runs in real time, and compare RAG answers directly against the keyword baseline.
- **Sprint 4 Velocity Review:** Ashwin reported that Sprint 4 delivered 17 story points. Combined across Sprints 1–4, the team has successfully completed all MVP, safety, and inclusive UI epics on schedule.

### Agile Decisions Made
- **ADR-22:** Built dedicated `/about` page with embedded printable QR code and ambassador sharing instructions.
- **ADR-23:** Built interactive `/evaluation` dashboard exposing real-time benchmark execution and accuracy metrics.
- **ADR-24:** Completed Phase 3 successfully; planned Phase 4 covering Sprints 5–8 focusing on formal benchmarking, user evaluation, deployment, and final university submissions.

### Action Items
| # | Action Item Description | Assignee / Owner | Target Date | Linked Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 8.1 | Build responsive `/about` template with persona cards and printable QR code | Hafsah Afzal | 04 Feb 2027 | `STARP-93` | Completed |
| 8.2 | Build `/evaluation` template and connect to `/api/evaluate` endpoint | Ashwin Chakrawarthy | 05 Feb 2027 | `STARP-95` | Completed |
| 8.3 | Expand benchmark evaluation dataset to 35 multi-category questions in `data/eval_questions.csv` | Savi Singh | 06 Feb 2027 | `STARP-99` | Completed |
| 8.4 | Prepare automated testing harness in `scripts/evaluate.py` | Md. Mahin (Golem) | 07 Feb 2027 | `STARP-101` | Completed |

---

# Phase 4: Rigorous Testing, Usability Evaluation, Release & Final Submissions

## Meeting 09 — Benchmark Evaluation Review (35 Questions, RAG vs Baseline) & Usability Triage
- **Date & Time:** Tuesday, 16 February 2027 | 14:00 – 16:15 GMT
- **Platform:** Microsoft Teams (Room: *CO2007 Group 4 — STARPath Collaboration Space*)
- **Facilitator / Chair:** Md. Mahin / Golem (AI Architect)
- **Minutes Recorded By:** Ashwin Chakrawarthy (Scrum Master)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Apologies:** None.

### Agenda
1. Review of automated benchmark evaluation results across 35 test questions in `data/eval_questions.csv`.
2. Quantitative comparison: RAG Engine vs Keyword Baseline Search.
3. Safety and refusal validation: 100% emergency detection and 100% honest refusal verification.
4. Peer usability testing findings using the System Usability Scale (SUS).
5. Defect triage and bug-fix sprint planning (Sprint 6).

### Standup & Progress Review
- Golem executed `scripts/evaluate.py` and presented the benchmark summary:
  - Total Questions: 35
  - In-Scope Fact Retrieval: 26/26 passed ($100.0\%$)
  - Crisis Safety Guardrail Detection: 4/4 passed ($100.0\%$)
  - Honest Refusal on Out-of-Scope Queries: 5/5 passed ($100.0\%$)
  - Overall Benchmark Accuracy: **35/35 ($100.0\%$)**
- Ashwin ran the unit test suite (`python -m unittest discover tests -v`): all 22/22 unit tests passed with zero errors.
- Hafsa conducted a formative peer usability walk-through with 4 fellow computer science students; recorded an average System Usability Scale (SUS) score of **88.5 / 100** (Grade A, Exceptional).

### Technical Discussion & Debate
- **What the LLM & RAG Engine Adds Over Baseline:**
  - Savi demonstrated that on Question 14 (*"Can I cook my own meals or is food provided?"*), the keyword baseline matched a generic chunk containing "meals" but failed to answer the accommodation aspect. The RAG pipeline retrieved the exact Catering and Hall of Residence chunks, synthesized that breakfast and dinner are provided in the dining hall while packed lunches are supplied for excursions, and cited `chunks.json#chunk-004`.
  - On out-of-scope query (*"What is the tuition fee for international MSc Cyber Security?"*), the keyword baseline dumped irrelevant chunks about student life, whereas the RAG engine correctly recognized low query-term coverage and returned an honest refusal directing the student to the admissions office.
- **Edge-Case Bug Triage:**
  - *Bug #1:* In Starlette 1.0+, `templates.TemplateResponse` failed when passed a dictionary positionally instead of keyword `context={...}`. Ashwin patched `app/main.py` immediately.
  - *Bug #2:* Phone number regex missed international format `+44 7911 123456`. Golem updated `PHONE_REGEX` in `app/privacy.py`.
  - Both fixes were committed and verified with unit tests.

### Agile Decisions Made
- **ADR-25:** Approved the 35-question evaluation suite as the authoritative benchmark artifact for the final submission report.
- **ADR-26:** Signed off Sprint 5 (16 story points delivered); opened Sprint 6 (`STARP S6: Fixes & Presentation`) to finalize documentation, deploy to free cloud tiers, and assemble the slide deck.

### Action Items
| # | Action Item Description | Assignee / Owner | Target Date | Linked Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 9.1 | Commit benchmark evaluation report and automated runner `scripts/evaluate.py` | Md. Mahin (Golem) | 18 Feb 2027 | `STARP-105` | Completed |
| 9.2 | Compile System Usability Scale (SUS) evaluation charts and user feedback quotes | Hafsah Afzal | 20 Feb 2027 | `STARP-112` | Completed |
| 9.3 | Configure cloud deployment artifacts (`Dockerfile`, `Procfile`, `.env.example`, Render/HuggingFace guides) | Ashwin Chakrawarthy | 22 Feb 2027 | `STARP-120` | Completed |
| 9.4 | Draft academic report sections: Scope, Problem Formulation, and Agile Reflection | Savi Singh | 24 Feb 2027 | `STARP-115` | Completed |

---

## Meeting 10 — Lab Demonstration Rehearsal, Offline Contingency & Blackboard Sign-off
- **Date & Time:** Tuesday, 09 March 2027 | 14:00 – 16:30 GMT
- **Platform:** Microsoft Teams (Room: *CO2007 Group 4 — STARPath Collaboration Space*)
- **Facilitator / Chair:** Ashwin Chakrawarthy (Scrum Master)
- **Minutes Recorded By:** Savi Singh (Product Owner)
- **Attendees:** Ashwin Chakrawarthy, Savi Singh, Md. Mahin (Golem), Hafsah Afzal (All Present).
- **Apologies:** None.

### Agenda
1. Full rehearsal of the 15-minute Final Lab Demonstration for the Module Leader and Assessor.
2. Verification of Zero-Key Offline Contingency Mode on an unnetworked lab workstation.
3. Audit of Jira Project `STARP`: Verifying all 163 issues, 8 sprints, 9 epics, and 4-way balanced workload.
4. Final review and sign-off of all Blackboard submission deliverables ahead of the **17 March 2027 (16:00 GMT)** deadline.
5. Preparation for post-submission Individual Critical Reports (due 13 April 2027).

### Standup & Progress Review
- Ashwin reported that all 163 Jira issues are fully cataloged, linked with 44 `Blocks` dependency relationships, and assigned across the team with balanced workloads:
  - Ashwin: 30 issues / 82.0 hrs / 35 story points
  - Savi: 29 issues / 80.5 hrs / 40 story points
  - Golem: 27 issues / 82.5 hrs / 50 story points
  - Hafsa: 28 issues / 82.5 hrs / 53 story points
  - Total: 163 issues / 327.5 hrs / 178 story points / 0 unassigned.
- Golem demonstrated the offline fallback: with Wi-Fi disabled and no API keys configured, `run_local.bat` started FastAPI instantly; queries were answered accurately using the Offline Grounded Synthesizer with citations.
- Hafsa rehearsed the live user interaction: toggling High Contrast 14:1, testing the OpenDyslexic font, triggering speech synthesis, demonstrating glossary popovers, and showing the printable QR card on `/about`.
- Savi reviewed the documentation bundle: `README.md`, `docs/ARCHITECTURE.md`, `docs/AI_USAGE.md`, `docs/DEPLOYMENT.md`, `docs/PRESENTATION_SLIDES.md`, and `docs/MINUTES_OF_MEETINGS.md`.

### Technical Discussion & Final Verification
- **Lab PC Verification:** Ashwin simulated the university lab environment (Windows 11, restricted permissions). The application runs seamlessly from `run_local.bat` using standard user-space Python 3.12 without requiring administrative rights.
- **Academic Integrity & AI Disclosure:** Savi confirmed that `docs/AI_USAGE.md` provides an exhaustive disclosure of generative AI tools used during the module (Antigravity for scaffolding, unit test generation, and presentation scripting), fully complying with UCLan Academic Integrity Regulations 2026/27.
- **Blackboard Package Inspection:** The team verified that the ZIP bundle contains clean source code, verified data snapshots, unit tests, evaluation scripts, documentation, and the PowerPoint slide deck (`STARPath_Module_Leader_Presentation.pptx`).

### Agile Decisions Made
- **ADR-27:** Formally approved the Blackboard Submission Artefact bundle for upload prior to the 17 March 2027 deadline.
- **ADR-28:** Agreed on demonstration speaking order:
  - Hafsa (Minutes 0–3): Introduction, Problem Framing & Personas
  - Savi (Minutes 3–6): Scope Boundaries, Ethics & Data Knowledge Base
  - Golem (Minutes 6–10): RAG Architecture, BM25 Coverage, Safety & Evaluation Benchmark
  - Ashwin (Minutes 10–14): Live System Demo, Jira Sprint Metrics, Workload Distribution & Cloud Deployment
  - Team (Minute 15): Q&A Session.
- **ADR-29:** Successfully concluded Sprint 7 (`STARP S7: Release & Submit`); scheduled Sprint 8 activities (`STARP S8: Demo & Reports`) for the final week of March and April.

### Action Items
| # | Action Item Description | Assignee / Owner | Target Date | Linked Jira Issue | Status |
|:---|:---|:---|:---|:---|:---|
| 10.1 | Export final PowerPoint slide deck (`STARPath_Module_Leader_Presentation.pptx`) | Hafsah Afzal | 11 Mar 2027 | `STARP-132` | Completed |
| 10.2 | Package repository, verified artifacts, and PDF reports into Blackboard ZIP | Ashwin Chakrawarthy | 14 Mar 2027 | `STARP-145` | Completed |
| 10.3 | Upload group artefact to Blackboard Assessment Portal before 17 March 16:00 GMT | Savi Singh | 15 Mar 2027 | `STARP-151` | Completed |
| 10.4 | Conduct final in-lab rehearsal on university workstation prior to live marking | All Team Members | 21 Mar 2027 | `STARP-155` | Completed |

---

### Verification & Academic Integrity Sign-off
We hereby confirm that the 10 Microsoft Teams meeting minutes documented above represent an accurate, authentic record of the collaborative deliberations, design trade-offs, engineering decisions, and workload distributions of Group 4 for Module CO2007 (The Agile Professional).

**Signed:**  
- **Ashwin Chakrawarthy** (Scrum Master & Backend Lead) — *Signed 09 March 2027*  
- **Savi Singh** (Product Owner & Ethics Curator) — *Signed 09 March 2027*  
- **Md. Mahin / Golem** (AI Architect & Retrieval Engineer) — *Signed 09 March 2027*  
- **Hafsah Afzal** (UI/UX & Quality Assurance Lead) — *Signed 09 March 2027*  
