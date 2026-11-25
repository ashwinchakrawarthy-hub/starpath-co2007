# STARPath System Architecture & Design Documentation

## 1. System Overview

**STARPath** is an accessible, privacy-preserving question-and-answer assistant designed for offer-holders on the University of Central Lancashire's (UCLan) Student Transition and Residential (STAR) programme. 

The application uses **Retrieval-Augmented Generation (RAG)** over a dated snapshot of approved public UCLan support web pages to ensure accurate, non-hallucinated answers with verifiable source page citations.

```mermaid
flowchart TD
    User(["Student / User (Browser)"]) -->|Query| API["FastAPI Web Server (/api/ask)"]
    API --> Safety{"Crisis Guardrail Check<br/>(safety.py)"}
    
    Safety -->|Crisis Detected| Wellbeing["Immediate Wellbeing Signposting<br/>(Bypasses LLM - 01772 893020 / 116 123)"]
    Wellbeing --> Response(["Structured JSON Response"])
    
    Safety -->|Safe Query| Privacy["PII Redaction Filter<br/>(privacy.py)"]
    Privacy -->|Sanitized Query| Retriever["Hybrid BM25 & Semantic Retriever<br/>(retriever.py)"]
    
    Retriever <--> KB[("Dated UCLan Knowledge Base<br/>(data/chunks.json)")]
    Retriever --> Threshold{"Score >= Threshold?<br/>(Coverage >= 0.28)"}
    
    Threshold -->|Out of Scope| Honest["Honest Refusal Guard<br/>('Could not find on approved pages')"]
    Honest --> Response
    
    Threshold -->|In Scope (Top-3 Chunks)| LLMConnector["Swappable LLM Connector<br/>(llm.py)"]
    
    LLMConnector -->|Config: gemini| Gemini["Google Gemini Free Tier API"]
    LLMConnector -->|Config: ollama| Ollama["Local Ollama Server"]
    LLMConnector -->|Config: offline / fallback| Fallback["Offline Grounded Synthesizer"]
    
    Gemini --> Formatter["Response Formatter & Glossary Tooltip Matcher"]
    Ollama --> Formatter
    Fallback --> Formatter
    
    Formatter --> Response
```

---

## 2. Component Architecture

### A. Web Layer (`app/main.py`)
- Built on **FastAPI** with asynchronous request handling.
- Serves semantic HTML5 templates rendered via **Jinja2** and static assets (`/static/css/style.css`, `/static/js/chat.js`).
- Exposes RESTful endpoints:
  - `POST /api/ask`: Core RAG execution endpoint.
  - `POST /api/simplify`: Plain-English simplification for international students.
  - `GET /api/glossary`: Full 30+ term university glossary.
  - `GET /api/baseline`: Pure keyword match without LLM synthesis (benchmarking).
  - `GET /api/evaluate`: Automated evaluation comparing RAG vs. Keyword Baseline over 35 test questions.
  - `GET /health`: Health status probe for cloud platforms.

### B. Safety & Crisis Guardrail (`app/safety.py`)
- Uses deterministic multi-pattern regular expressions to detect severe distress, crisis, or self-harm.
- **Rule Enforcement:** Completely bypasses the language model to prevent unsafe or hallucinated amateur therapy.
- Directly signposts the UCLan Mental Health and Wellbeing Service (01772 893020, `wellbeing@uclan.ac.uk`), Campus Security 24/7 (01772 892068), NHS 111, Samaritans (116 123), and Papyrus (0800 068 4141).

### C. Privacy & Anonymity Filter (`app/privacy.py`)
- Detects and replaces emails, UK phone numbers, 8-digit UCLan student IDs, payment cards, and postcodes with redaction tokens before passing prompts to any language model.
- Server logging records only execution timestamps and error codes; question content is never persisted to disk.

### D. Knowledge Base & Hybrid Retriever (`app/retriever.py`)
- Pre-indexes dated text chunks from 8 approved UCLan web pages.
- Calculates BM25 Inverse Document Frequency:
  $$\text{IDF}(t) = \max\left(0.2, \ln\left(\frac{N - \text{df} + 0.5}{\text{df} + 0.5} + 1.0\right)\right)$$
- Incorporates **query token coverage penalty**:
  $$\text{Score} = \frac{\text{BM25Score} \times \text{Coverage}^{1.5}}{\sqrt{|\text{QueryTokens}|}}$$
- Employs a strict threshold (`SIMILARITY_THRESHOLD = 0.18`) and coverage guard (`Coverage >= 0.28`) to trigger honest refusal for out-of-scope questions without hallucination.

### E. Swappable LLM Connector (`app/llm.py`)
- Provides a unified `generate_rag_answer()` interface controlled by a single setting (`LLM_PROVIDER`):
  1. `gemini`: Free Google Gemini API (`gemini-1.5-flash`).
  2. `ollama`: Local open-source model server.
  3. `offline`: 100% local grounded extractive synthesizer that operates with zero keys and zero internet access.
- Implements resilient fallbacks: if an external service is unavailable or rate-limited, the system falls back to the offline synthesizer rather than failing.

---

## 3. Accessibility Compliance (WCAG 2.2 AA)

- **Display Themes:** Four distinct color themes including High Contrast Yellow/Black (14:1+ contrast) and Color-Blind Safe (Blue/Amber palette).
- **Text Sizing:** Dynamic font scaling (Small, Standard, Large, Extra Large).
- **Dyslexia Support:** One-click toggle for dyslexia-friendly typography with increased word and line spacing.
- **Screen Reader Support:** Semantic HTML5 (`header`, `main`, `aside`, `nav`, `footer`), skip-to-content links, and dynamic ARIA live regions (`aria-live="polite"`).
- **Speech Synthesis:** Built-in Web Speech API read-aloud functionality for low-vision and neurodivergent students.
