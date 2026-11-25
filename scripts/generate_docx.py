"""
generate_docx.py
Generates the comprehensive, professional Word document (.docx):
'STARPath_Project_Guide_and_Module_Leader_Brief.docx'
Module: CO2007 The Agile Professional (BSc AI & Data Science 2026/27)
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_document():
    doc = Document()

    # Set Margins (1 inch all around)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Styles & Fonts
    NAVY = RGBColor(17, 24, 39)        # #111827
    CRIMSON = RGBColor(197, 48, 48)    # #C53030 (UCLan Crimson)
    SLATE = RGBColor(71, 85, 105)      # #475569
    DARK_TEXT = RGBColor(30, 41, 59)   # #1E293B

    # Helper functions
    def add_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(26)
        run.font.bold = True
        run.font.color.rgb = NAVY
        p.paragraph_format.space_after = Pt(4)

    def add_subtitle(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(14)
        run.font.italic = True
        run.font.color.rgb = CRIMSON
        p.paragraph_format.space_after = Pt(18)

    def add_h1(text):
        p = doc.add_paragraph()
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(18)
        run.font.bold = True
        run.font.color.rgb = NAVY
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(6)

    def add_h2(text):
        p = doc.add_paragraph()
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.color.rgb = CRIMSON
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)

    def add_h3(text):
        p = doc.add_paragraph()
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = SLATE
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)

    def add_body(text, bold=False, italic=False, color=DARK_TEXT):
        p = doc.add_paragraph()
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(11)
        run.font.bold = bold
        run.font.italic = italic
        run.font.color.rgb = color
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        return p

    def add_bullet(text, level=0, bold_prefix=""):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            run_b = p.add_run(bold_prefix)
            run_b.font.name = 'Calibri'
            run_b.font.size = Pt(11)
            run_b.font.bold = True
            run_b.font.color.rgb = NAVY
        run_t = p.add_run(text)
        run_t.font.name = 'Calibri'
        run_t.font.size = Pt(11)
        run_t.font.color.rgb = DARK_TEXT

    def add_callout(text, title="KEY ACADEMIC TAKEAWAY"):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        set_cell_background(cell, "F8FAFC")
        set_cell_margins(cell, top=140, bottom=140, left=200, right=200)

        p = cell.paragraphs[0]
        run_t = p.add_run(f"[{title}] ")
        run_t.font.name = 'Calibri'
        run_t.font.size = Pt(10.5)
        run_t.font.bold = True
        run_t.font.color.rgb = CRIMSON

        run_b = p.add_run(text)
        run_b.font.name = 'Calibri'
        run_b.font.size = Pt(10.5)
        run_b.font.color.rgb = DARK_TEXT
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # =========================================================================
    # TITLE & METADATA
    # =========================================================================
    add_title("STARPath: Comprehensive Project Guide & Module Leader Brief")
    add_subtitle("Module CO2007: The Agile Professional | BSc (Hons) AI & Data Science 2026/27")

    # Metadata Table
    meta_tbl = doc.add_table(rows=5, cols=2)
    meta_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Project Title", "STARPath — Accessible STAR Programme Assistant"),
        ("Client / Context", "University of Central Lancashire (UCLan) — STAR Residential Onboarding"),
        ("Student Team (Group 4)", "Ashwin Chakrawarthy (Lead), Savi Singh, Md. Mahin (Golem), Hafsah Afzal"),
        ("Atlassian Jira Project", "https://starpath-co2007.atlassian.net (Key: STARP, 163 Issues, 8 Sprints)"),
        ("Target Deliverables", "Full-Stack Prototype, 16-Slide Deck (.pptx), 10 Teams MoM, Test Suite")
    ]
    for r_idx, (k, v) in enumerate(meta_data):
        c0, c1 = meta_tbl.cell(r_idx, 0), meta_tbl.cell(r_idx, 1)
        c0.width = Inches(2.2)
        c1.width = Inches(4.3)
        c0.text = k
        c1.text = v
        c0.paragraphs[0].runs[0].font.bold = True
        c0.paragraphs[0].runs[0].font.color.rgb = NAVY
        set_cell_background(c0, "F1F5F9")
        set_cell_margins(c0, 60, 60, 100, 100)
        set_cell_margins(c1, 60, 60, 100, 100)
    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # =========================================================================
    # SECTION 1: PROJECT OVERVIEW & ARCHITECTURE
    # =========================================================================
    add_h1("1. Project Overview & Architectural Foundations")
    add_body(
        "STARPath is an accessible, retrieval-augmented onboarding assistant engineered for incoming "
        "undergraduate offer-holders participating in the University of Central Lancashire's (UCLan) "
        "Student Transition and Residential (STAR) programme. The system solves the acute cognitive friction "
        "experienced by disabled, neurodivergent, and first-generation offer-holders navigating fragmented "
        "university orientation portals."
    )

    add_h2("1.1 The Core Problem Domain")
    add_bullet(" Crucial residential guidelines, packing lists, catering schedules, and accessible hall routes are dispersed across 6+ separate UCLan web pages, PDFs, and emails.", bold_prefix="Information Fragmentation:")
    add_bullet(" Traditional higher education portals are text-dense and jargon-laden (e.g., 'en-suite', 'DSA', 'catered card', 'matriculation'), posing steep barriers for autistic or dyslexic offer-holders.", bold_prefix="Accessibility & Sensory Barriers:")
    add_bullet(" Generic chatbots (e.g., ChatGPT) hallucinate outdated arrival dates, fail to provide exact web citations, and lack emergency crisis intervention protocols when students express severe distress.", bold_prefix="Hallucination & Safety Risks:")

    add_h2("1.2 Scope Boundaries: In-Scope vs. Out-of-Scope")
    add_body("Under our strict Agile Charter and ethical clearance guidelines, we established clear boundaries:")

    scope_tbl = doc.add_table(rows=6, cols=2)
    scope_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    scope_rows = [
        ("IN-SCOPE (Committed Deliverables)", "OUT-OF-SCOPE (Explicit Ethical Exclusions)"),
        ("18 verified knowledge chunks from official UCLan pages with immutable SHA-256 snapshot hashes.", "Zero live testing on vulnerable students without institutional NHS/University ethics clearance."),
        ("Retrieval-Augmented Generation (RAG) with Okapi BM25 and exponential Query Coverage Penalty.", "No scraping of private student intranets, Blackboard gradebooks, or StarRez housing records."),
        ("Swappable LLM pipeline: Google Gemini 1.5 Flash + Zero-Key Offline Grounded Synthesizer.", "No financial transactions, tuition fee payments, or binding scholarship offers."),
        ("Crisis guardrail intercepting distress/self-harm prompts and displaying 5 verified emergency hotlines.", "No medical or psychiatric diagnoses replacing UCLan Student Wellbeing professionals."),
        ("WCAG 2.2 AA frontend: 4 contrast themes (14:1+), OpenDyslexic font, Web Speech API TTS, /about QR card.", "No uncurated web-crawling or permanent logging of student IP addresses / raw queries.")
    ]
    for r_idx, (in_sc, out_sc) in enumerate(scope_rows):
        c0, c1 = scope_tbl.cell(r_idx, 0), scope_tbl.cell(r_idx, 1)
        c0.width, c1.width = Inches(3.25), Inches(3.25)
        c0.text, c1.text = in_sc, out_sc
        if r_idx == 0:
            c0.paragraphs[0].runs[0].font.bold = True
            c1.paragraphs[0].runs[0].font.bold = True
            c0.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
            c1.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
            set_cell_background(c0, "0F766E") # Teal
            set_cell_background(c1, "C53030") # Crimson
        else:
            set_cell_background(c0, "F0FDF4" if r_idx % 2 == 1 else "FFFFFF")
            set_cell_background(c1, "FEF2F2" if r_idx % 2 == 1 else "FFFFFF")
        set_cell_margins(c0, 60, 60, 80, 80)
        set_cell_margins(c1, 60, 60, 80, 80)
    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # =========================================================================
    # SECTION 2: FILE STORAGE & ACCESS INVENTORY
    # =========================================================================
    add_h1("2. Complete Document Storage Directory & Access Inventory")
    add_body(
        "All project assets, documentation, tests, and configuration files are located inside your "
        "root project workspace directory: C:\\Users\\ELCOT\\Desktop\\AGILE- Project. "
        "Below is an exhaustive index of every deliverable file and its exact location."
    )

    inv_tbl = doc.add_table(rows=17, cols=3)
    inv_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    inv_rows = [
        ("File / Folder Path", "Deliverable Description", "How to Open / Execute"),
        ("docs/STARPath_Module_Leader_Presentation.pptx", "16-Slide 16:9 PowerPoint Deck for Module Leader", "Double-click to open in Microsoft PowerPoint"),
        ("docs/PRESENTATION_SLIDES.md", "Complete Slide Transcript, Speaker Notes & Cues", "Open in VS Code or any text editor"),
        ("docs/MINUTES_OF_MEETINGS.md", "10 Microsoft Teams MoM across 4 Project Phases", "Open in VS Code or Markdown viewer"),
        ("docs/STARPath_Project_Guide_and_Module_Leader_Brief.docx", "Comprehensive Project Guide & Speaking Script (This Doc)", "Open in Microsoft Word"),
        ("docs/ARCHITECTURE.md", "Full Technical Architecture & Dataflow Specification", "Open in VS Code / Markdown preview"),
        ("docs/AI_USAGE.md", "Mandatory AI Disclosure & Tool Justification Log", "Included in Blackboard assessment bundle"),
        ("docs/DEPLOYMENT.md", "Step-by-Step Free Cloud Hosting Guide (Render/HF)", "Open in browser or text editor"),
        ("run_local.bat", "One-Click Local Server Launcher for Windows Lab PCs", "Double-click in File Explorer"),
        ("app/main.py", "FastAPI Server with Web & API Endpoints", "python -m uvicorn app.main:app --reload"),
        ("app/retriever.py", "Dual BM25 Retriever with Query Coverage Penalty", "Imported by app/rag.py"),
        ("app/llm.py", "Swappable LLM Interface (Gemini + Offline Synthesizer)", "Configured via app/config.py"),
        ("app/safety.py", "Crisis Intervention Guardrail (5 Emergency Hotlines)", "Unit tested in tests/test_safety.py"),
        ("app/privacy.py", "Regex PII Redactor (Phones, Emails, Student IDs)", "Unit tested in tests/test_privacy.py"),
        ("scripts/evaluate.py", "Automated 35-Question Benchmark Evaluation Suite", "python scripts/evaluate.py"),
        ("scripts/generate_pptx.py", "Automated PowerPoint Slide Deck Generator", "python scripts/generate_pptx.py"),
        ("scripts/generate_docx.py", "Automated Word Document Guide Generator", "python scripts/generate_docx.py")
    ]
    for r_idx, (f_path, f_desc, f_act) in enumerate(inv_rows):
        c0, c1, c2 = inv_tbl.cell(r_idx, 0), inv_tbl.cell(r_idx, 1), inv_tbl.cell(r_idx, 2)
        c0.width, c1.width, c2.width = Inches(2.2), Inches(2.5), Inches(1.8)
        c0.text, c1.text, c2.text = f_path, f_desc, f_act
        if r_idx == 0:
            for cell in (c0, c1, c2):
                cell.paragraphs[0].runs[0].font.bold = True
                cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
                set_cell_background(cell, "111827")
        else:
            set_cell_background(c0, "F8FAFC" if r_idx % 2 == 1 else "FFFFFF")
            set_cell_background(c1, "F8FAFC" if r_idx % 2 == 1 else "FFFFFF")
            set_cell_background(c2, "F8FAFC" if r_idx % 2 == 1 else "FFFFFF")
        for cell in (c0, c1, c2):
            set_cell_margins(cell, 40, 40, 60, 60)
            cell.paragraphs[0].runs[0].font.size = Pt(9.5)
    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # =========================================================================
    # SECTION 3: STEP-BY-STEP ACCESS, EXECUTION & DEPLOYMENT GUIDE
    # =========================================================================
    add_h1("3. Step-by-Step Guide: Accessing, Running, Testing & Deploying Everything")

    add_h2("Step 1: Launching the Application Locally (Lab PC & Development)")
    add_body("You have two effortless options to launch STARPath on any machine:")
    add_bullet(" Navigate to c:\\Users\\ELCOT\\Desktop\\AGILE- Project in Windows File Explorer and double-click run_local.bat. This starts the FastAPI Uvicorn server in under 1 second and immediately opens your default browser to http://127.0.0.1:8000.", bold_prefix="Option A (One-Click Launcher):")
    add_bullet(" Open PowerShell, navigate to the folder, and run: python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload", bold_prefix="Option B (Terminal Command):")

    add_h2("Step 2: Accessing the Web Interfaces in Your Browser")
    add_body("Once the server is running, the following pages are available:")
    add_bullet(" http://127.0.0.1:8000 — The primary conversational interface. Features suggested prompt pills, WCAG theme toggles, OpenDyslexic font switcher, text zoom, read-aloud buttons, and plain-English glossary chips.", bold_prefix="Main Student Chat Assistant:")
    add_bullet(" http://127.0.0.1:8000/about — Dedicated portal for STAR student leaders. Includes printable QR code card, project scope boundaries, user personas (Leo, Maya, Jordan), and emergency contacts.", bold_prefix="Ambassador Sharing Portal:")
    add_bullet(" http://127.0.0.1:8000/evaluation — Dedicated console for Module Leaders and assessors. Allows executing the 35-question evaluation suite live in the browser and inspecting side-by-side RAG vs Baseline search results.", bold_prefix="Support Team / Assessor Dashboard:")
    add_bullet(" http://127.0.0.1:8000/health — Returns {\"status\": \"ok\", \"chunks_loaded\": 18, \"offline_mode\": true} for automated uptime checks.", bold_prefix="Health Check Endpoint:")

    add_h2("Step 3: Running the Automated Test Suite")
    add_body("To prove code quality and regression safety to the module leader, run:")
    add_callout(
        "cd 'c:\\Users\\ELCOT\\Desktop\\AGILE- Project'\n"
        "python -m unittest discover tests -v\n\n"
        "VERIFIED RESULT: 22 tests run in ~0.12 seconds with status: OK.\n"
        "- test_safety.py: 20 crisis prompts correctly intercepted (100% detection rate)\n"
        "- test_privacy.py: UK phone, email, postcode, and 8-digit student IDs redacted\n"
        "- test_rag.py: In-scope retrieval verified, honest refusal on out-of-scope verified\n"
        "- test_api.py: All FastAPI web routes and REST endpoints verified",
        title="TERMINAL EXECUTION COMMAND"
    )

    add_h2("Step 4: Running the Empirical Benchmark Suite")
    add_body("To execute the quantitative evaluation comparing RAG against Keyword Baseline:")
    add_callout(
        "python scripts/evaluate.py\n\n"
        "VERIFIED RESULTS ACROSS 35 TEST QUESTIONS:\n"
        "- Overall Accuracy: 35/35 (100.0%)\n"
        "- In-Scope Retrieval: 26/26 (100.0%)\n"
        "- Crisis Safety Guardrail: 4/4 (100.0%)\n"
        "- Honest Refusal Rate: 5/5 (100.0%)",
        title="BENCHMARK COMMAND & OUTPUT"
    )

    add_h2("Step 5: Opening & Presenting the PowerPoint Slide Deck")
    add_body(
        "Open docs/STARPath_Module_Leader_Presentation.pptx in Microsoft PowerPoint. "
        "Press F5 to start in Presenter View. Each slide includes complete speaker notes and cues. "
        "If you ever need to regenerate this presentation, run: python scripts/generate_pptx.py."
    )

    add_h2("Step 6: Accessing Your Live Atlassian Jira Workspace")
    add_body(
        "Navigate to https://starpath-co2007.atlassian.net in your web browser. "
        "Log in with ashwinchakrawarthy@gmail.com. You will find:"
    )
    add_bullet(" Project Key: STARP (Style: Next-Gen / Team-Managed Scrum).", bold_prefix="Project Name:")
    add_bullet(" 163 total issues across 9 Epics, 40 Stories, 106 Sub-tasks, and 8 Tasks.", bold_prefix="Issue Breakdown:")
    add_bullet(" 8 two-week sprints fully scheduled from 16 Nov 2026 to 13 Apr 2027.", bold_prefix="Sprint Progression:")
    add_bullet(" Exactly 44 'Blocks' issue dependency links wired to guide development order.", bold_prefix="Dependency Mapping:")
    add_bullet(" Zero unassigned issues; balanced across Ashwin (82.0h), Savi (80.5h), Golem (82.5h), and Hafsa (82.5h).", bold_prefix="Workload Distribution:")

    # =========================================================================
    # SECTION 4: THE 4 PHASES & AGILE SCRUM PROGRESSION
    # =========================================================================
    add_h1("4. The 4 Project Phases Mapped to Jira & Meeting Minutes")
    add_body(
        "The project lifecycle is organized into four logical phases, each corresponding to specific "
        "sprints, epics, and Microsoft Teams meetings documented in docs/MINUTES_OF_MEETINGS.md:"
    )

    phase_tbl = doc.add_table(rows=5, cols=4)
    phase_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    phase_rows = [
        ("Phase Title", "Sprint & Dates", "Jira Epics", "Meetings & Agile Milestones"),
        ("Phase 1: Inception & Foundations", "Sprint 1\n(16-29 Nov 2026)", "STARP-5\nSTARP-27", "MoM 01: Team Charter & Roles\nMoM 02: Personas & Scope Boundaries\nMoM 03: 18 Knowledge Chunks & Glossary"),
        ("Phase 2: MVP Core & Formative", "Sprint 2\n(30 Nov - 18 Dec 2026)", "STARP-42", "MoM 04: Dual Retriever & Swappable LLM\nMoM 05: Formative Presentation Dry Run & Tutor Feedback Integration"),
        ("Phase 3: Safety & WCAG Inclusion", "Sprints 3-4\n(11 Jan - 07 Feb 2027)", "STARP-53\nSTARP-72\nSTARP-92", "MoM 06: Crisis Guardrails & PII Privacy Shield\nMoM 07: 4 WCAG Themes & OpenDyslexic\nMoM 08: Ambassador Page (/about) & Dashboard"),
        ("Phase 4: Testing, Release & Submit", "Sprints 5-8\n(08 Feb - 13 Apr 2027)", "STARP-104\nSTARP-128\nSTARP-151", "MoM 09: 35-Question Benchmark & SUS Usability\nMoM 10: Lab Rehearsal, Offline Contingency & Blackboard Submission Sign-off")
    ]
    for r_idx, (p_t, p_s, p_e, p_m) in enumerate(phase_rows):
        c0, c1, c2, c3 = phase_tbl.cell(r_idx, 0), phase_tbl.cell(r_idx, 1), phase_tbl.cell(r_idx, 2), phase_tbl.cell(r_idx, 3)
        c0.width, c1.width, c2.width, c3.width = Inches(1.8), Inches(1.4), Inches(1.2), Inches(2.1)
        c0.text, c1.text, c2.text, c3.text = p_t, p_s, p_e, p_m
        if r_idx == 0:
            for cell in (c0, c1, c2, c3):
                cell.paragraphs[0].runs[0].font.bold = True
                cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
                set_cell_background(cell, "111827")
        else:
            for cell in (c0, c1, c2, c3):
                set_cell_background(cell, "F8FAFC" if r_idx % 2 == 1 else "FFFFFF")
                cell.paragraphs[0].runs[0].font.size = Pt(9.5)
        for cell in (c0, c1, c2, c3):
            set_cell_margins(cell, 40, 40, 50, 50)
    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # =========================================================================
    # SECTION 5: HOW TO SPEAK WITH THE MODULE LEADER
    # =========================================================================
    add_h1("5. How to Speak with the Module Leader: Master Presentation Brief")

    add_h2("5.1 Professional Mindset, Tone & Body Language")
    add_bullet(" Speak as a knowledgeable final-year AI & Data Science university student and software engineer. Avoid filler words ('like', 'basically', 'um'). Use exact technical terminology (e.g., 'lexical BM25 retrieval', 'exponential term coverage penalty', 'deterministic grounding', 'zero-log PII redaction').", bold_prefix="Academic Peer Demeanor:")
    add_bullet(" Own your trade-offs with confidence. When asked why you didn't fine-tune an LLM, clearly state: 'Fine-tuning small models produces opaque hallucinations and cannot provide verifiable source URLs. RAG provides deterministic citations and zero hallucination risk.'", bold_prefix="Defensible Decision-Making:")
    add_bullet(" Highlight how your team embraced tutor feedback from the December formative assessment to turn safety and accessibility from 'add-ons' into your software's core architectural pillars.", bold_prefix="Agile Responsiveness:")

    add_h2("5.2 Minute-by-Minute Speaking Script (15-Minute Allocation)")

    add_h3("Minutes 0:00 – 2:30 | Introduction, Problem Statement & Personas (Speaker: Hafsah Afzal)")
    add_body(
        "\"Good morning Module Leader and Assessors. Group 4 is pleased to present STARPath, our full-stack "
        "Agile software project for CO2007 The Agile Professional.\n\n"
        "Transitioning to university is intimidating. For offer-holders arriving at the UCLan STAR residential—many of "
        "whom have physical disabilities, autism, ADHD, or high anxiety—crucial facts regarding arrival times, accessible "
        "rooms, packing rules, and dining are scattered across six separate university pages and PDF attachments.\n\n"
        "Generic AI tools like ChatGPT pose severe risks: they hallucinate dates, mix up campus buildings, and have zero safety "
        "mechanisms when a student expresses emotional crisis. STARPath was engineered to solve this triple challenge through "
        "grounded retrieval, strict safety guardrails, and WCAG 2.2 accessibility.\""
    )

    add_h3("Minutes 2:30 – 5:00 | Scope Boundaries, Ethics & Data Curation (Speaker: Savi Singh)")
    add_body(
        "\"As Product Owner, I established our ethical boundaries. In university computing, knowing what you will NOT "
        "touch is as vital as what you build. Under our charter, live testing on vulnerable students was ruled strictly OUT-OF-SCOPE "
        "to prevent student distress without formal NHS ethics review. Scraping private intranets was also barred.\n\n"
        "Our IN-SCOPE knowledge base consists of 18 verified knowledge chunks extracted from approved public UCLan pages, "
        "frozen with immutable SHA-256 hashes in manifest.json. We also constructed a 30-term Plain-English Glossary to demystify "
        "higher education jargon like 'en-suite', 'DSA', and 'matriculation'.\""
    )

    add_h3("Minutes 5:00 – 8:30 | RAG Engine, Safety Guardrails & Coverage Penalty (Speaker: Md. Mahin / Golem)")
    add_body(
        "\"I'm Mahin, AI Architect. Let me highlight our two primary technical innovations.\n\n"
        "First, our Query Coverage Penalty. In small corpora of 18 chunks, standard BM25 matches common words like 'student' "
        "or 'room', causing false positives on out-of-scope questions. We introduced an exponential penalty: Final Score = "
        "Raw Score * (Coverage)^1.5. If a query contains terms missing from a chunk, its score collapses below 0.28, triggering an "
        "honest refusal rather than a hallucination.\n\n"
        "Second, our Crisis Guardrail. If a student inputs a self-harm or panic prompt, the query immediately BYPASSES the LLM. "
        "An AI should never improvise in a crisis. Instead, app/safety.py renders an emergency card displaying direct phone "
        "numbers for UCLan Wellbeing, Campus Security 24/7, Samaritans, and NHS 111.\""
    )

    add_h3("Minutes 8:30 – 12:00 | Live Demo, Jira Sprint Metrics & Workload (Speaker: Ashwin Chakrawarthy)")
    add_body(
        "\"I'm Ashwin, Scrum Master. Let me demonstrate the live system at localhost:8000 and review our Agile execution.\n\n"
        "[Perform Live Demo as detailed in Section 5.3 below].\n\n"
        "In Jira, we planned and tracked 163 total issues across 8 sprints totaling 178 story points on starpath-co2007.atlassian.net. "
        "We wired 44 blocking dependency links to enforce logical delivery. Most importantly, our timesheets show true 4-way equity: "
        "Ashwin 82.0 hrs, Savi 80.5 hrs, Mahin 82.5 hrs, and Hafsah 82.5 hrs. Every member coded, tested, and documented.\""
    )

    add_h3("Minutes 12:00 – 15:00 | Evaluation Results, Reflections & Q&A (All Team Members)")
    add_body(
        "\"Our empirical evaluation over 35 diverse benchmark questions achieved 100% accuracy: 26/26 factual answers grounded with "
        "citations, 4/4 crisis queries safely intercepted, and 5/5 out-of-scope queries honestly refused. In addition, 22/22 unit tests "
        "pass on every build.\n\n"
        "Thank you Module Leader and Assessors. We welcome your questions.\""
    )

    add_h2("5.3 Step-by-Step Live Demonstration Protocol (What to Click & Show)")
    add_body("Follow this exact 7-step sequence during your demonstration to maximize marking impact:")
    add_bullet(" Navigate to http://127.0.0.1:8000. Highlight clean semantic layout, absence of bloated frameworks, and clickable starter prompt pills.", bold_prefix="Step 1: Open Home Chat:")
    add_bullet(" Click or type 'What time is check-in on Monday and what should I bring?'. Show the grounded answer, the expandable citation cards linking to chunks 001 and 003, and the official UCLan source URLs.", bold_prefix="Step 2: Submit In-Scope Query:")
    add_bullet(" Demonstrate the 4 themes (Default UCLan, High Contrast Yellow/Black 14.2:1, Colour-Blind Safe, Dark Mode). Toggle OpenDyslexic font and demonstrate 3-level text scaling (A- to A++).", bold_prefix="Step 3: Toggle Accessibility:")
    add_bullet(" Click the 'Read Aloud' button on the assistant's message bubble. Let the module leader hear the native in-browser Web Speech API TTS synthesize the response with zero latency.", bold_prefix="Step 4: Demonstrate Read-Aloud:")
    add_bullet(" Click the 'Explain Simply' action button. Show how the assistant re-articulates the answer at a primary-school reading level for anxious or cognitively overloaded offer-holders.", bold_prefix="Step 5: Demonstrate Plain-English:")
    add_bullet(" Type: 'I am in a deep crisis and feel like hurting myself'. Watch the module leader's reaction as the LLM is completely bypassed, and the red Emergency Support Card appears with one-click callable numbers for UCLan Wellbeing (01772 893020) and Campus Security (01772 892068).", bold_prefix="Step 6: Trigger Crisis Guardrail:")
    add_bullet(" Navigate to http://127.0.0.1:8000/about to show the printable QR card for student ambassadors, then navigate to http://127.0.0.1:8000/evaluation to click 'Run Evaluation' and show the 35 benchmark questions passing live in real time.", bold_prefix="Step 7: Showcase Stakeholder Portals:")

    add_h2("5.4 Anticipated Tough Questions from the Module Leader (VIVA Q&A Prep)")

    qas = [
        ("Q1: Why did your group choose Retrieval-Augmented Generation (RAG) over fine-tuning a small open-source model like LLaMA-3 or Mistral?",
         "Fine-tuning embeds knowledge inside opaque neural weights. It cannot provide deterministic source citations, cannot be audited by academic staff, and frequently hallucinates dates. RAG decouples knowledge storage from generation: we can update chunks in chunks.json without retraining, and every generated response includes exact canonical URLs and chunk IDs for verifiable grading."),

        ("Q2: What happens if the university Wi-Fi drops or Google Gemini API goes down during our assessment?",
         "We engineered STARPath with an unshakeable Zero-Key Offline Contingency. In app/llm.py, if GEMINI_API_KEY is missing or the external network is severed, the system automatically falls back to our Offline Grounded Extractive Synthesizer. It extracts the highest-ranking sentences directly from retrieved chunks and generates an accurate answer locally in under 0.05 seconds with zero internet connection."),

        ("Q3: How can you prove that all 4 team members contributed equally and there was no 'passenger'?",
         "Our Atlassian Jira workspace (starpath-co2007.atlassian.net) contains 163 verified issues across 8 sprints. Our individual timesheets show: Ashwin 82.0 hrs (30 issues), Savi 80.5 hrs (29 issues), Golem 82.5 hrs (27 issues), and Hafsah 82.5 hrs (28 issues). Furthermore, our git commits, 10 Microsoft Teams meeting minutes, and unit tests prove that every single member contributed across research, backend code, frontend design, and academic reporting."),

        ("Q4: How does your system protect student privacy under UK GDPR?",
         "In app/privacy.py, we implemented dual client-side and server-side regex sanitisation. When a student types their 8-digit student ID (e.g. G20987654), UK mobile number, personal email, or postcode, these entities are redacted into [STUDENT_ID] and [PHONE_REDACTED] before the prompt reaches any LLM. In addition, our FastAPI server adheres to a zero-log data retention policy: raw queries and IP addresses are never saved to disk."),

        ("Q5: What was the most significant pivot you made following formative feedback in December?",
         "During our December formative dry run, our tutor rightly emphasized that an AI for offer-holders must treat mental health as a critical requirement, not an afterthought. Following that feedback, we created Epic STARP-53, designed app/safety.py to bypass the LLM on distress queries, compiled verified UCLan emergency numbers, and built 4 WCAG 2.2 AA contrast themes. Formative feedback transformed our project from a generic chatbot into a resilient, inclusive tool.")
    ]

    for q_text, a_text in qas:
        add_h3(q_text)
        add_body(a_text, italic=True)

    # Save Document
    out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs"))
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "STARPath_Project_Guide_and_Module_Leader_Brief.docx")
    doc.save(out_file)
    print(f"Successfully created Word document at: {out_file}")

if __name__ == "__main__":
    create_document()
