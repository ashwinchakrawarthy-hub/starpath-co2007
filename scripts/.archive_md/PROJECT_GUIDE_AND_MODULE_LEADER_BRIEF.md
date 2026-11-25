# STARPath — Comprehensive Project Guide, File Directory & Module Leader Presentation Brief
## Module: CO2007 The Agile Professional (BSc AI & Data Science 2026/27)

> **Document Type:** Step-by-Step System Manual & Presentation Guide  
> **Native Word File (.docx):** [`docs/STARPath_Project_Guide_and_Module_Leader_Brief.docx`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/docs/STARPath_Project_Guide_and_Module_Leader_Brief.docx)  
> **PowerPoint Slide Deck (.pptx):** [`docs/STARPath_Module_Leader_Presentation.pptx`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/docs/STARPath_Module_Leader_Presentation.pptx)  
> **Jira Project Workspace:** [`https://starpath-co2007.atlassian.net`](https://starpath-co2007.atlassian.net) (Key: `STARP`, Board: `STARP Board`)  
> **Team Members (Group 4):** Ashwin Chakrawarthy (Lead), Savi Singh, Md. Mahin (Golem), Hafsah Afzal  

---

## 1. Project Overview & Problem Formulation

### 1.1 The Challenge
Incoming undergraduate offer-holders on the University of Central Lancashire's (**UCLan**) **Student Transition, Academic Readiness (STAR) programme** face three major onboarding hurdles:
1. **Scattered Information:** Vital residential facts regarding arrival times, luggage drop-offs, catering times, and accessible hall routes are dispersed across six different UCLan portals, PDF attachments, and emails.
2. **Cognitive Overload & Jargon:** Higher education terminology like *DSA*, *en-suite*, *STAR Leader*, *catered card*, and *matriculation* causes distress for neurodivergent (autistic/dyslexic) and first-generation offer-holders.
3. **The AI Hallucination & Crisis Danger:** Commercial tools like ChatGPT hallucinate arrival dates, fabricate non-existent room policies, and lack emergency crisis intervention protocols when a student expresses acute distress.

### 1.2 Our Solution
**STARPath** is an accessible, privacy-preserving, grounded Retrieval-Augmented Generation (RAG) assistant:
- **Zero Hallucination:** Answers are grounded exclusively in an approved 18-chunk snapshot of official UCLan web pages (`data/chunks.json` verified with SHA-256 hashes in `data/manifest.json`).
- **Term Coverage Penalty:** Okapi BM25 scores are weighted by query coverage: $\text{Final Score} = \text{Raw Score} \times (\text{Coverage})^{1.5}$. If key query terms are missing, the score collapses below $0.28$, triggering an honest refusal instead of a hallucination.
- **Crisis Intervention Guardrail:** Queries expressing self-harm or panic bypass the LLM completely to display emergency contact numbers (UCLan Wellbeing, Campus Security 24/7, Samaritans, NHS 111, Papyrus).
- **GDPR Privacy Shield:** Regex sanitisation strips UK phones, emails, 8-digit student IDs, and postcodes prior to retrieval.
- **Universal Accessibility (WCAG 2.2 AA):** 4 switchable contrast themes (including High Contrast 14.2:1), OpenDyslexic font toggle, 3-level text scaling, native Web Speech API read-aloud, and Plain-English glossary popovers.
- **Stakeholder Portals:** Ambassador sharing page ([`/about`](http://127.0.0.1:8000/about)) with printable QR card, and Support Team Dashboard ([`/evaluation`](http://127.0.0.1:8000/evaluation)) with live 35-question benchmarking.

---

## 2. Master Directory of Project Documents & Storage Locations

All deliverables are organized in your project workspace: `c:\Users\ELCOT\Desktop\AGILE- Project\`.

| File / Folder Path | Deliverable Purpose | How to Open / Run |
|:---|:---|:---|
| [`docs/STARPath_Project_Guide_and_Module_Leader_Brief.docx`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/docs/STARPath_Project_Guide_and_Module_Leader_Brief.docx) | Comprehensive Word document guide & speaking manual | Double-click to open in Microsoft Word |
| [`docs/STARPath_Module_Leader_Presentation.pptx`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/docs/STARPath_Module_Leader_Presentation.pptx) | 16-Slide 16:9 widescreen PowerPoint deck | Double-click to open in PowerPoint |
| [`docs/PRESENTATION_SLIDES.md`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/docs/PRESENTATION_SLIDES.md) | Full slide transcript, speaker timings & layout notes | Open in VS Code or any text editor |
| [`docs/MINUTES_OF_MEETINGS.md`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/docs/MINUTES_OF_MEETINGS.md) | 10 Teams meeting minutes across 4 Project Phases | Open in Markdown viewer |
| [`docs/ARCHITECTURE.md`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/docs/ARCHITECTURE.md) | In-depth technical architecture & dataflow diagrams | Open in Markdown viewer |
| [`docs/AI_USAGE.md`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/docs/AI_USAGE.md) | Mandatory AI tool declaration & justification log | Included in Blackboard ZIP bundle |
| [`docs/DEPLOYMENT.md`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/docs/DEPLOYMENT.md) | Free cloud hosting guide (Render, Hugging Face, Cloudflare) | Open in browser or text editor |
| [`run_local.bat`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/run_local.bat) | One-click launcher for Windows lab workstations | Double-click in Windows File Explorer |
| [`app/main.py`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/app/main.py) | FastAPI application with web routes and REST endpoints | `python -m uvicorn app.main:app --reload` |
| [`app/retriever.py`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/app/retriever.py) | Dual BM25 retriever with query coverage penalty | Core RAG search module |
| [`app/llm.py`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/app/llm.py) | Swappable LLM pipeline (Gemini API + Offline Synthesizer) | Controlled via `app/config.py` |
| [`app/safety.py`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/app/safety.py) | Crisis detection guardrail (5 UK emergency contacts) | Unit tested in `tests/test_safety.py` |
| [`app/privacy.py`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/app/privacy.py) | Regex PII redaction shield (emails, phones, student IDs) | Unit tested in `tests/test_privacy.py` |
| [`data/chunks.json`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/data/chunks.json) | 18 approved UCLan knowledge chunks | Curated knowledge base |
| [`data/manifest.json`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/data/manifest.json) | Immutable collection snapshot with SHA-256 hashes | Verification manifest |
| [`data/glossary.json`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/data/glossary.json) | 30+ plain-English higher education definitions | Powering UI popovers |
| [`data/eval_questions.csv`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/data/eval_questions.csv) | 35 multi-domain benchmark test questions | Authoritative test dataset |
| [`scripts/evaluate.py`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/scripts/evaluate.py) | Automated 35-question benchmark evaluation runner | `python scripts/evaluate.py` |
| [`scripts/generate_pptx.py`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/scripts/generate_pptx.py) | Python script that regenerates the PowerPoint deck | `python scripts/generate_pptx.py` |
| [`scripts/generate_docx.py`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/scripts/generate_docx.py) | Python script that regenerates the Word guide | `python scripts/generate_docx.py` |
| [`README.md`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/README.md) | Main repository documentation and quick start | Primary project index |
| [`GEMINI.md`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/GEMINI.md) | Academic persona rule (BSc AI & DS student profile) | Active workspace rule |

---

## 3. Step-by-Step Execution, Testing & Demonstration Guide

### Step 1: Start the Local Application
- **Method A (Easiest):** Double-click [`run_local.bat`](file:///c:/Users/ELCOT/Desktop/assesment1-%20ds/run_local.bat) in your project folder. The server boots in $<1$ second and opens your browser directly to `http://127.0.0.1:8000`.
- **Method B (PowerShell):**
  ```powershell
  cd "c:\Users\ELCOT\Desktop\AGILE- Project"
  python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
  ```

### Step 2: Access the Three Stakeholder Views
1. **Student Q&A Chat Assistant:** `http://127.0.0.1:8000/`
2. **Ambassador Sharing & QR Card Portal:** `http://127.0.0.1:8000/about`
3. **Module Leader Evaluation Dashboard:** `http://127.0.0.1:8000/evaluation`

### Step 3: Run the 22 Automated Unit Tests
To verify code integrity and prove absence of regression to the module leader:
```powershell
python -m unittest discover tests -v
```
*Expected Output:* **22/22 tests passed (OK) in ~0.12 seconds**.

### Step 4: Run the 35-Question Benchmark Suite
To show quantitative evaluation results:
```powershell
python scripts/evaluate.py
```
*Expected Output:*
- RAG Overall Accuracy: **35/35 (100.0%)**
- In-Scope Retrieval: **26/26 (100.0%)**
- Crisis Safety Interceptions: **4/4 (100.0%)**
- Honest Refusal on Out-of-Scope: **5/5 (100.0%)**

### Step 5: Access Your Live Jira Workspace
- URL: `https://starpath-co2007.atlassian.net`
- Log in with: `ashwinchakrawarthy@gmail.com`
- Navigate to: **Projects $\rightarrow$ STARPath (STARP) $\rightarrow$ Boards (STARP Board)**
- You will see all **163 issues** cleanly mapped across **8 sprints**, with **44 Blocks dependency links** and **0 unassigned issues**.

---

## 4. How to Speak with the Module Leader

### 4.1 Professional Speaking Guidelines
- **Demanded Tone:** Ambitious, articulate, technically sound final-year AI & Data Science university student.
- **Avoid Vague Jargon:** Do not say *"we used AI to answer stuff"*. Say: *"We implemented an asynchronous FastAPI service orchestrating an Okapi BM25 retriever enhanced with an exponential query term coverage penalty to eliminate false positives on low-resource corpora."*
- **Emphasize Agile Responsiveness:** Explain how formative feedback in December reshaped your backlog, elevating crisis safety and WCAG accessibility into core architectural constraints.

### 4.2 15-Minute Presentation Speaking Script

#### Minutes 0:00 – 2:30 | Introduction, Problem Statement & Personas (Speaker: Hafsah Afzal)
> *"Good morning Module Leader and Assessors. Group 4 presents STARPath, our full-stack Agile software project for CO2007 The Agile Professional.*
> 
> *Transitioning to university is intimidating. For offer-holders arriving at the UCLan STAR residential—many of whom have physical disabilities, autism, ADHD, or high anxiety—crucial facts regarding arrival times, accessible rooms, packing rules, and dining are scattered across six separate university pages and PDF attachments.*
> 
> *Generic AI tools like ChatGPT pose severe risks: they hallucinate dates, mix up campus buildings, and have zero safety mechanisms when a student expresses emotional crisis. STARPath was engineered to solve this triple challenge through grounded retrieval, strict safety guardrails, and WCAG 2.2 accessibility."*

#### Minutes 2:30 – 5:00 | Scope Boundaries, Ethics & Data Curation (Speaker: Savi Singh)
> *"As Product Owner, I established our ethical boundaries. In university computing, knowing what you will NOT touch is as vital as what you build. Under our charter, live testing on vulnerable students was ruled strictly OUT-OF-SCOPE to prevent student distress without formal NHS ethics review. Scraping private intranets was also barred.*
> 
> *Our IN-SCOPE knowledge base consists of 18 verified knowledge chunks extracted from approved public UCLan pages, frozen with immutable SHA-256 hashes in manifest.json. We also constructed a 30-term Plain-English Glossary to demystify higher education jargon like 'en-suite', 'DSA', and 'matriculation'."*

#### Minutes 5:00 – 8:30 | RAG Engine, Safety Guardrails & Coverage Penalty (Speaker: Md. Mahin / Golem)
> *"I'm Mahin, AI Architect. Let me highlight our two primary technical innovations.*
> 
> *First, our Query Coverage Penalty. In small corpora of 18 chunks, standard BM25 matches common words like 'student' or 'room', causing false positives on out-of-scope questions. We introduced an exponential penalty: $\text{Final Score} = \text{Raw Score} \times (\text{Coverage})^{1.5}$. If a query contains terms missing from a chunk, its score collapses below 0.28, triggering an honest refusal rather than a hallucination.*
> 
> *Second, our Crisis Guardrail. If a student inputs a self-harm or panic prompt, the query immediately BYPASSES the LLM. An AI should never improvise in a crisis. Instead, app/safety.py renders an emergency card displaying direct phone numbers for UCLan Wellbeing, Campus Security 24/7, Samaritans, and NHS 111."*

#### Minutes 8:30 – 12:00 | Live Demo, Jira Sprint Metrics & Workload (Speaker: Ashwin Chakrawarthy)
> *"I'm Ashwin, Scrum Master. Let me demonstrate the live system at localhost:8000 and review our Agile execution.*
> 
> *[Perform Live Demo using the 7-step sequence below].*
> 
> *In Jira, we planned and tracked 163 total issues across 8 sprints totaling 178 story points on starpath-co2007.atlassian.net. We wired 44 blocking dependency links to enforce logical delivery. Most importantly, our timesheets show true 4-way equity: Ashwin 82.0 hrs, Savi 80.5 hrs, Mahin 82.5 hrs, and Hafsah 82.5 hrs. Every member coded, tested, and documented."*

#### Minutes 12:00 – 15:00 | Evaluation Results, Reflections & Q&A (All Team Members)
> *"Our empirical evaluation over 35 diverse benchmark questions achieved 100% accuracy: 26/26 factual answers grounded with citations, 4/4 crisis queries safely intercepted, and 5/5 out-of-scope queries honestly refused. In addition, 22/22 unit tests pass on every build.*
> 
> *Thank you Module Leader and Assessors. We welcome your questions."*

---

### 4.3 Step-by-Step Live Demonstration Protocol (7-Step Sequence)

1. **Open Home Chat:** Open `http://127.0.0.1:8000`. Point out the clean semantic HTML5 layout, no bloated frameworks, and clickable starter questions.
2. **Submit In-Scope Query:** Click *"What time is check-in on Monday and what should I bring?"*. Point out the grounded answer, the expandable citation card linking to chunks 001 and 003, and the official UCLan source URLs.
3. **Toggle Accessibility Controls:** Switch between the 4 themes (Default UCLan, High Contrast Yellow/Black 14.2:1, Colour-Blind Safe, Dark Mode). Toggle the OpenDyslexic font and demonstrate 3-level text scaling ($A^-$ to $A^{++}$).
4. **Demonstrate Speech Synthesis:** Click the **"Read Aloud"** button on the assistant bubble. Let the module leader hear the native in-browser Web Speech API TTS synthesize the response instantly with zero server lag.
5. **Demonstrate Plain-English:** Click the **"Explain Simply"** button on the bot card. Show how the assistant re-articulates the answer at a primary-school reading level for anxious offer-holders.
6. **Trigger Crisis Guardrail:** Type: *"I am in a deep crisis and feel like hurting myself"*. Show how the LLM is completely bypassed, and the red Emergency Support Card appears with one-click callable numbers for UCLan Wellbeing (`01772 893020`) and Campus Security (`01772 892068`).
7. **Showcase Stakeholder Portals:**
   - Go to `http://127.0.0.1:8000/about` to show the printable QR card for student ambassadors.
   - Go to `http://127.0.0.1:8000/evaluation` to click **"Run Evaluation"** and show the 35 benchmark questions passing live in real time.

---

### 4.4 Defending Tough Questions (VIVA Q&A Preparation)

- **Q1: Why RAG instead of fine-tuning an open-source model like LLaMA-3?**  
  *Answer:* *"Fine-tuning embeds knowledge into opaque neural weights, making it impossible to audit, update quickly, or provide verifiable source URLs. It also frequently hallucinates dates. RAG decouples knowledge storage from generation: we can update chunks in chunks.json without retraining, and every generated response includes exact canonical URLs and chunk IDs for verifiable grading."*

- **Q2: What happens if campus Wi-Fi drops during our assessment?**  
  *Answer:* *"STARPath features an unshakeable Zero-Key Offline Contingency. If GEMINI_API_KEY is missing or internet is unavailable, app/llm.py automatically falls back to our Offline Grounded Extractive Synthesizer. It extracts the highest-ranking sentences directly from retrieved chunks and generates an accurate answer locally in under 0.05 seconds with zero internet connection."*

- **Q3: How do you prove all 4 members contributed equally?**  
  *Answer:* *"Our Jira workspace contains 163 verified issues across 8 sprints. Our individual timesheets show: Ashwin 82.0 hrs (30 issues), Savi 80.5 hrs (29 issues), Golem 82.5 hrs (27 issues), and Hafsah 82.5 hrs (28 issues). Furthermore, our git commits, 10 Microsoft Teams meeting minutes, and unit tests prove that every single member contributed across research, backend code, frontend design, and academic reporting."*

- **Q4: How does your system comply with UK GDPR?**  
  *Answer:* *"In app/privacy.py, we implemented dual client-side and server-side regex sanitisation. When a student types their 8-digit student ID (e.g. G20987654), UK mobile number, personal email, or postcode, these entities are redacted into [STUDENT_ID] and [PHONE_REDACTED] before the prompt reaches any LLM. In addition, our FastAPI server adheres to a zero-log data retention policy: raw queries and IP addresses are never saved to disk."*

- **Q5: What was the most significant pivot from formative feedback?**  
  *Answer:* *"During our December formative dry run, our tutor rightly emphasized that an AI for offer-holders must treat mental health as a critical requirement, not an afterthought. Following that feedback, we created Epic STARP-53, designed app/safety.py to bypass the LLM on distress queries, compiled verified UCLan emergency numbers, and built 4 WCAG 2.2 AA contrast themes. Formative feedback transformed our project from a generic chatbot into a resilient, inclusive tool."*
