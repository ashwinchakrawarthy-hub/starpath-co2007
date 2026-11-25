# Artificial Intelligence Usage & Acknowledgement Log

**Module:** CO2007 The Agile Professional  
**Course:** BSc (Hons) Artificial Intelligence and Data Science (Academic Year 2026/27)  
**Project:** STARPath - Accessible STAR Programme Assistant  
**Team Members:** Ashwin, Savi, Golem, Hafsa  

---

## 1. Compliance Statement

In compliance with **Section 7 (Information on Artificial Intelligence)** of the CO2007 module brief and the university's Academic Integrity policy, this document records where and how Artificial Intelligence (AI) tools were utilized during the development of the product, along with academic and technical justifications.

> *Note: In accordance with university regulations, AI tools are strictly permitted for product development where acknowledged and justified, but are **NOT permitted** for the writing of the individual critical report.*

---

## 2. Product-Level AI Usage (The Product Itself)

As defined in the project brief, the product itself is an AI assistant exploring the potential of language models for supporting disabled students:

| Component | Model / Technology | Source / Provider | Academic & Technical Justification |
|---|---|---|---|
| **Retrieval-Augmented Generation (RAG)** | Dual BM25 + Term TF-IDF & Coverage Scorer | Custom In-House Python Implementation | Prevents hallucination by constraining answers strictly to retrieved passages from approved public UCLan web pages. |
| **Language Model Connector (Primary Online)** | Google Gemini (`gemini-1.5-flash`) | Google AI Studio (Free Tier) | High-speed, high-context window, zero-cost online generation capable of synthesizing multi-passage answers with source page citations. |
| **Language Model Connector (Local Offline)** | Ollama (`llama3.2`) | Local Open Source Model Server | Demonstrates self-hosted data sovereignty and resilience if internet connectivity is unavailable during campus demonstrations. |
| **Resilient Grounded Fallback** | Deterministic Extractive Synthesizer | Custom In-House Python Algorithm | Ensures 100% operational uptime during live lab demonstrations even if free-tier API quotas are exhausted or network access fails. |

---

## 3. Development-Assisting AI Usage Log

| Date | Development Area | AI Tool Used | Scope of Contribution | Human Review & Verification |
|---|---|---|---|---|
| 2026-11-11 | Project Planning & Work Breakdown | Generative Coding Assistant | Assisted with drafting Jira WBS task descriptions, acceptance criteria, and time estimation balances. | Team reviewed all 163 items, verified balanced workloads (80.5h–82.5h), and approved in Jira. |
| 2026-11-12 | Safety Guardrail Pattern Engineering | Generative Coding Assistant | Generated initial regex test prompts for crisis detection. | Team cross-referenced against UCLan Wellbeing Service emergency numbers and verified 100% test pass rate in `test_safety.py`. |
| 2026-11-12 | CSS Accessible Contrast Styling | Generative Coding Assistant | Suggested CSS variable structures for WCAG 2.2 AA multi-theme palette. | Validated using WebAIM contrast checker to ensure `>= 4.5:1` contrast across all four themes. |
| 2026-11-12 | Evaluation Suite Scripting | Generative Coding Assistant | Boilerplate generation for side-by-side RAG vs Keyword Baseline evaluation. | Refined similarity scoring, IDF smoothing, and coverage formulas to ensure accurate honest refusal. |

---

## 4. Academic Integrity Sign-Off

The code committed in this repository represents the genuine collaborative work of Ashwin, Savi, Golem, and Hafsa. No proprietary, internal, or private third-party code was used. All public web page contents used in the knowledge base originated exclusively from approved public UCLan web pages.
