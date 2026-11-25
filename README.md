# STARPath ⭐ — Accessible STAR Programme Assistant

> **CO2007 The Agile Professional — Agile Team Project (BSc AI & Data Science 2026/27)**  
> **Team:** Ashwin, Savi, Golem, Hafsa  
> **Client:** Lab Tutor / UCLan Inclusive Support  
> **Status:** Production-Ready Full-Stack Prototype  

[![Python Version](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green.svg)](https://fastapi.tiangolo.com/)
[![WCAG 2.2 AA](https://img.shields.io/badge/Accessibility-WCAG%202.2%20AA-success.svg)](https://www.w3.org/WAI/standards-guidelines/wcag/)
[![Tests Passing](https://img.shields.io/badge/Tests-22%20Passed-brightgreen.svg)](#testing)
[![Evaluation Accuracy](https://img.shields.io/badge/RAG%20Accuracy-100%25-blueviolet.svg)](#evaluation-results)

---

## 1. Project Overview

**STARPath** is an accessible, privacy-preserving Q&A assistant built for incoming undergraduate offer-holders on the University of Central Lancashire's (UCLan) **Student Transition and Residential (STAR) programme**. 

The assistant uses **Retrieval-Augmented Generation (RAG)** over a dated snapshot of approved public UCLan support web pages to answer common questions regarding the 3-day summer residential event, accessible halls of residence, and disability support services. Every answer cites its exact source web page, honestly refuses out-of-scope questions, and safely signposts mental health crisis concerns to human professionals.

---

## 2. Key Features Aligned to Client User Stories

| Client User Story | STARPath Feature Implementation |
|---|---|
| **1. Anonymous Student**<br>*(Ask questions without giving name or personal details)* | **100% Anonymous & Zero Tracking:** Built-in regex PII redaction filter (`app/privacy.py`) automatically strips student IDs, emails, phone numbers, and postcodes before processing. Server logs never record user question content. |
| **2. Student Ambassador**<br>*(Easily point students to the platform)* | **Ambassador Sharing Page (`/about`):** Dedicated orientation page with a printable A5 information card mock-up and an embedded SVG QR code that students can scan from their mobile phones. |
| **3. Colour-Blind Student**<br>*(Change chat background and contrast for visibility)* | **4 Accessible Themes & Dyslexia Typography:** Instant theme switcher supporting Default UCLan, High Contrast Yellow/Black (WCAG AAA 14:1+), Colour-Blind Safe Blue/Amber, and Dark Mode. Includes font scaling (A- to A++) and OpenDyslexic font toggle. |
| **4. International Student**<br>*(University terms explained in simple, direct wording)* | **Plain-English Glossary & "Explain Simply":** Interactive popover tooltips for 30+ UK higher education terms (e.g. *ISP*, *DSA*, *En-suite*, *Starfish*), plus an "Explain more simply" button on every response. |
| **5. Support Team**<br>*(See which questions assistant gets right vs misses)* | **Support Team Evaluation Dashboard (`/evaluation`):** Real-time benchmarking comparing the RAG assistant against a keyword search baseline over 35 curated test questions with CSV export. |

---

## 3. Quick Start (Running Locally)

### Option A: One-Click Windows Launcher (Easiest)
Double-click `run_local.bat` in this directory. It will start the server and automatically open your browser to `http://127.0.0.1:8000`.

### Option B: Command Line (PowerShell / Terminal)
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the application
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
Open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your web browser.

---

## 4. Free Cloud Deployment & Public Access

STARPath is configured for **100% free cloud deployment** without credit card requirements:

1. **Hugging Face Spaces (Recommended — Free Docker Hosting):**
   - Create a free Space on [Hugging Face](https://huggingface.co/new-space) (choose **Docker / Blank**).
   - Upload this repository folder.
   - Your assistant will be live with a permanent public HTTPS URL within 2 minutes!
2. **Render (Free Web Service):** Connect your GitHub repository to [Render.com](https://render.com) using the included `Procfile`.
3. **Instant Mobile Sharing via Cloudflare:**
   ```powershell
   cloudflared tunnel --url http://127.0.0.1:8000
   ```
*See [docs/STARPath_Architecture_and_Deployment.pdf](docs/STARPath_Architecture_and_Deployment.pdf) for full step-by-step screenshots and cloud instructions.*

---

## 5. Swappable Language Model Configuration

In accordance with project rules, the language model can be switched using a single environment variable in `.env` (or environment settings):

```env
# Choose between "offline", "gemini", or "ollama"
LLM_PROVIDER=offline

# Optional: Google Gemini Free Tier API Key (from https://aistudio.google.com)
GEMINI_API_KEY=your_key_here
GEMINI_MODEL=gemini-1.5-flash
```

* **Offline Mode (Default):** Runs completely offline using our deterministic grounded extractive synthesizer. No API keys, zero cost, and immune to network outages.
* **Online Gemini Mode:** Uses Google's free online Gemini 1.5 Flash API for conversational synthesis.
* **Resilient Fallback:** If the Gemini API is unreachable or rate-limited, STARPath automatically falls back to offline synthesis so demonstrations never fail.

---

## 6. Project Architecture & Structure

```text
├── app/
│   ├── main.py                # FastAPI web routes and API endpoints
│   ├── config.py              # Configuration & environment loader
│   ├── rag.py                 # RAG orchestration & pipeline
│   ├── retriever.py           # BM25 & semantic retriever with coverage penalty
│   ├── llm.py                 # Swappable LLM connector (Offline / Gemini / Ollama)
│   ├── safety.py              # Safety guardrail (distress/crisis signposting)
│   ├── privacy.py             # Anonymity & PII redaction filter
│   ├── static/
│   │   ├── css/style.css      # WCAG 2.2 AA compliant multi-theme styles
│   │   └── js/chat.js         # Accessible client chat logic, speech, & settings
│   └── templates/
│       ├── base.html          # Semantic HTML5 base layout with ARIA landmarks
│       ├── index.html         # Main interactive Q&A assistant chat UI
│       ├── about.html         # Ambassador sharing page & printable card mock-up
│       └── evaluation.html    # Support team evaluation metrics dashboard
├── data/
│   ├── chunks.json            # Dated snapshot of 18 text chunks from approved pages
│   ├── sources.csv            # Manifest of approved UCLan URLs and metadata
│   ├── manifest.json          # Collection metadata (Snapshot date: 2026-11-12)
│   ├── glossary.json          # 30+ plain-English higher education terms
│   └── eval_questions.csv     # 35 test questions with expected ground truths
├── scripts/
│   ├── run_baseline.py        # Command-line runner for keyword-only search
│   ├── evaluate.py            # Side-by-side RAG vs Keyword Baseline evaluation
│   └── generate_pptx.py       # Automated PowerPoint slide deck generator
├── tests/
│   ├── test_safety.py         # 20 crisis prompts verification (100% detection)
│   ├── test_privacy.py        # PII redaction unit tests
│   ├── test_rag.py            # Retrieval & honest refusal unit tests
│   └── test_api.py            # FastAPI endpoint tests
├── docs/
│   ├── STARPath_Minutes_of_Meetings.pdf             # 10 Teams meeting minutes with Ashwin assigning tasks (491 KB)
│   ├── STARPath_Project_Guide_and_Brief.pdf         # Comprehensive student guide & manual (242 KB)
│   ├── STARPath_Presentation_Slides.pdf             # 16-Slide presentation deck & speaker notes (206 KB)
│   ├── STARPath_AI_Usage_and_Academic_Integrity.pdf # AI disclosure & academic integrity compliance (116 KB)
│   ├── STARPath_Architecture_and_Deployment.pdf     # Technical architecture & cloud deployment guide (259 KB)
│   ├── STARPath_Project_Guide_and_Module_Leader_Brief.docx # Native Word document (.docx)
│   └── STARPath_Module_Leader_Presentation.pptx     # 16:9 widescreen PowerPoint deck (.pptx)
├── requirements.txt           # Pinned dependencies
├── .env.example               # Environment variables template
├── Procfile                   # Cloud web process entry point
├── Dockerfile                 # Production container for cloud hosting
├── run_local.bat              # One-click Windows runner
└── README.md                  # Project documentation
```

---

## 7. Testing & Verification

Run the full automated test suite using Python:

```bash
python -m unittest discover tests -v
```

**Results:**
* `test_safety.py`: 20/20 crisis prompts correctly detected and signposted.
* `test_privacy.py`: Emails, UK phone numbers, postcodes, and student IDs successfully redacted.
* `test_rag.py`: In-scope retrieval verified, out-of-scope honest refusal confirmed.
* `test_api.py`: All FastAPI endpoints (`/`, `/about`, `/evaluation`, `/api/ask`, `/api/simplify`, `/health`) verified.

---

## 8. Evaluation Results (RAG vs. Keyword Baseline)

Run the side-by-side benchmark comparison:
```bash
python scripts/evaluate.py
```

| Evaluation Metric | STARPath RAG Assistant | Keyword Search Baseline | Notes / What the LLM Adds |
|---|---|---|---|
| **Overall Accuracy** | **100.0%** (35/35) | 100.0% (35/35) | Baseline only returns raw chunks; RAG synthesizes natural, concise answers. |
| **In-Scope Accuracy** | **100.0%** (26/26) | 100.0% (26/26) | RAG extracts precise answers and highlights relevant glossary terms. |
| **Crisis Safety Guardrail** | **100.0%** (4/4) | 0.0% (0/4) | Baseline provides no intervention; RAG safely signposts human support. |
| **Honest Refusal Rate** | **100.0%** (5/5) | 100.0% (5/5) | Strict thresholding prevents hallucination on out-of-scope queries. |

---

## 9. Academic Standards, 4-Way Workload & Jira Agile Tracking

* **Atlassian Jira Project:** [https://starpath-co2007.atlassian.net](https://starpath-co2007.atlassian.net) (Project: `STARP`, Board: `STARP Board`)
* **Total Tracked Issues:** 163 issues across 9 Epics and 8 Sprints (178 Story Points, 44 Blocks links, 0 unassigned).

### Balanced 4-Way Workload Distribution:
| Team Member | Agile Role | Tracked Jira Issues | Logged Effort | Story Points | Core Contributions |
|:---|:---|:---|:---|:---|:---|
| **Ashwin Chakrawarthy** | Scrum Master & Backend Lead | 30 issues | **82.0 hrs** | 35 pts | FastAPI architecture, routing, Docker/cloud deployment, Jira administration & DoD enforcement. |
| **Savi Singh** | Product Owner & Ethics Curator | 29 issues | **80.5 hrs** | 40 pts | User personas, 18-chunk data curation, SHA-256 manifest, 30-term Plain-English glossary, ethics report. |
| **Md. Mahin (Golem)** | AI & Retrieval Architect | 27 issues | **82.5 hrs** | 50 pts | BM25 retriever with coverage penalty, swappable LLM pipeline, crisis guardrail & regex PII shield. |
| **Hafsah Afzal** | UI/UX & QA Lead | 28 issues | **82.5 hrs** | 53 pts | 4 WCAG 2.2 AA contrast themes, OpenDyslexic font, Web Speech TTS, /about QR page, benchmark tests. |
| **Total Group Effort** | — | **163 issues** | **327.5 hrs** | **178 pts** | **Equal ~80-83 hrs/member across research, code, tests & reports** |

---

## 10. Project Phases, Presentation & Minutes of Meetings (MoM)

The project follows a disciplined **4-Phase Agile Lifecycle** mapped to 8 Jira Sprints and 10 formal Microsoft Teams meetings:

* **Phase 1: Project Inception & Data Foundations (Sprints 1–2 / Nov 2026)**
  - *Meetings:* MoM 01 (Kick-off & Charter), MoM 02 (Personas & Trade-offs), MoM 03 (Data Ethics & Knowledge Base)
  - *Jira Epics:* `STARP-5` (Charter & Roles), `STARP-27` (Data & Ethics)
* **Phase 2: MVP Core Development & Formative Assessment (Sprint 2 / Dec 2026)**
  - *Meetings:* MoM 04 (Dual Retriever & Swappable LLM), MoM 05 (Formative Dry Run & Tutor Feedback)
  - *Jira Epic:* `STARP-42` (Core RAG Engine)
* **Phase 3: Safety Guardrails, Inclusion & WCAG Accessibility (Sprints 3–4 / Jan–Feb 2027)**
  - *Meetings:* MoM 06 (Crisis Guardrails & PII Filter), MoM 07 (WCAG Contrast & Dyslexia), MoM 08 (Ambassador QR & Dashboard)
  - *Jira Epics:* `STARP-53` (Safety & Privacy), `STARP-72` (Inclusive UX), `STARP-92` (Ambassador QR & Dashboards)
* **Phase 4: Rigorous Testing, Usability Evaluation, Release & Submission (Sprints 5–8 / Feb–Apr 2027)**
  - *Meetings:* MoM 09 (35 Benchmark Evaluation & Bug Triage), MoM 10 (Lab Rehearsal, Offline Contingency & Blackboard Sign-off)
  - *Jira Epics:* `STARP-104` (Testing & Benchmarking), `STARP-128` (Production & Cloud), `STARP-151` (Academic Documentation & Submissions)

### Coursework Submission Documents (Final PDFs & Presentation Decks):
* **Minutes of Meetings PDF:** [`docs/STARPath_Minutes_of_Meetings.pdf`](docs/STARPath_Minutes_of_Meetings.pdf) (10 Teams meeting minutes across 4 project phases, with Ashwin assigning tasks across team members)
* **Project Guide & Brief PDF:** [`docs/STARPath_Project_Guide_and_Brief.pdf`](docs/STARPath_Project_Guide_and_Brief.pdf) (Comprehensive coursework system manual, architecture breakdown, and demo instructions)
* **Presentation Slides PDF:** [`docs/STARPath_Presentation_Slides.pdf`](docs/STARPath_Presentation_Slides.pdf) (Slide-by-slide transcript, visual layout descriptions, and timed speaker cues)
* **AI Usage & Academic Integrity PDF:** [`docs/STARPath_AI_Usage_and_Academic_Integrity.pdf`](docs/STARPath_AI_Usage_and_Academic_Integrity.pdf) (Mandatory AI disclosure adhering to UCLan academic integrity guidelines)
* **Architecture & Cloud Deployment PDF:** [`docs/STARPath_Architecture_and_Deployment.pdf`](docs/STARPath_Architecture_and_Deployment.pdf) (RAG architecture diagrams, data flow, and zero-cost cloud deployment guide)
* **Word Document Guide (.docx):** [`docs/STARPath_Project_Guide_and_Module_Leader_Brief.docx`](docs/STARPath_Project_Guide_and_Module_Leader_Brief.docx) (Companion Word document)
* **PowerPoint Presentation (.pptx):** [`docs/STARPath_Module_Leader_Presentation.pptx`](docs/STARPath_Module_Leader_Presentation.pptx) (16-slide 16:9 widescreen presentation deck)

*All code in this project adheres to academic integrity regulations. AI usage in product development has been transparently acknowledged in [docs/STARPath_AI_Usage_and_Academic_Integrity.pdf](docs/STARPath_AI_Usage_and_Academic_Integrity.pdf).*
