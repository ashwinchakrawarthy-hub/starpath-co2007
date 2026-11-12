"""Swappable Language Model connector for STARPath.

Supports:
1. Google Gemini API (free online tier)
2. Local Ollama model (e.g., llama3.2, mistral)
3. Offline Grounded Synthesizer (100% zero-dependency local fallback, guaranteed to work offline)

All prompts strictly instruct the model to answer using ONLY the retrieved passages,
state when information is not present, and cite source titles.
"""
import json
import logging
import requests
from typing import List, Dict, Any, Tuple
from app.config import (
    LLM_PROVIDER,
    GEMINI_API_KEY,
    GEMINI_MODEL,
    OLLAMA_URL,
    OLLAMA_MODEL
)

logger = logging.getLogger("STARPath.LLM")

SYSTEM_INSTRUCTION = """You are STARPath, a helpful, honest, and accessible question-and-answer assistant for incoming students on UCLan's Student Transition and Residential (STAR) programme.

CRITICAL RULES:
1. Answer using ONLY the factual information in the provided Source Passages below.
2. If the answer is NOT present in the passages, you MUST say honestly: "I could not find information about that in the approved university support pages." Do NOT guess or invent facts.
3. Write in clear, straightforward, and supportive language with short sentences suitable for a diverse audience, including international students and neurodivergent students.
4. At the end of your answer, explicitly mention which page and section your answer came from.
5. If the user mentions distress or self-harm, direct them immediately to the UCLan Wellbeing Service."""


def format_context_prompt(query: str, retrieved_chunks: List[Dict[str, Any]]) -> str:
    """Format prompt with retrieved context passages."""
    passages_text = []
    for i, chunk in enumerate(retrieved_chunks, 1):
        passages_text.append(
            f"--- [PASSAGE {i}] ---\n"
            f"Page: {chunk.get('page_title', '')}\n"
            f"Section: {chunk.get('section', '')}\n"
            f"URL: {chunk.get('url', '')}\n"
            f"Content: {chunk.get('content', '')}\n"
        )

    context_block = "\n".join(passages_text)
    prompt = (
        f"SOURCE PASSAGES FROM APPROVED UCLAN WEB PAGES:\n"
        f"{context_block}\n\n"
        f"USER QUESTION: {query}\n\n"
        f"INSTRUCTION: Answer the user's question clearly and accurately using ONLY the information in the source passages above."
    )
    return prompt


def call_gemini_api(prompt: str, system_instruction: str = SYSTEM_INSTRUCTION) -> Tuple[str, str]:
    """Call Google Gemini REST API free tier with automatic model fallback."""
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not configured in .env or environment.")

    candidate_models = [GEMINI_MODEL]
    if "gemini-3.1-flash-lite" not in candidate_models:
        candidate_models.append("gemini-3.1-flash-lite")
    if "gemini-flash-lite-latest" not in candidate_models:
        candidate_models.append("gemini-flash-lite-latest")

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ],
        "systemInstruction": {
            "parts": [{"text": system_instruction}]
        },
        "generationConfig": {
            "temperature": 0.2,
            "maxOutputTokens": 600,
            "topP": 0.8
        }
    }

    last_error = None
    for model_name in candidate_models:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={GEMINI_API_KEY}"
        try:
            resp = requests.post(url, json=payload, timeout=20)
            if resp.status_code == 200:
                data = resp.json()
                candidates = data.get("candidates", [])
                if candidates and "content" in candidates[0]:
                    parts = candidates[0]["content"].get("parts", [])
                    if parts and "text" in parts[0]:
                        return parts[0]["text"].strip(), f"Google Gemini ({model_name})"
            else:
                last_error = f"Model {model_name} returned HTTP {resp.status_code}: {resp.text[:120]}"
                logger.warning("Gemini model %s failed, attempting next candidate: %s", model_name, last_error)
        except Exception as e:
            last_error = str(e)
            logger.warning("Exception calling Gemini model %s: %s", model_name, e)

    raise RuntimeError(f"All Gemini models exhausted. Last error: {last_error}")


def call_ollama_api(prompt: str, system_instruction: str = SYSTEM_INSTRUCTION) -> Tuple[str, str]:
    """Call local Ollama endpoint."""
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "system": system_instruction,
        "stream": False,
        "options": {
            "temperature": 0.2
        }
    }

    resp = requests.post(OLLAMA_URL, json=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    response_text = data.get("response", "").strip()
    if response_text:
        return response_text, f"Ollama Local ({OLLAMA_MODEL})"

    raise RuntimeError("Empty response from Ollama")


def offline_grounded_synthesizer(query: str, retrieved_chunks: List[Dict[str, Any]]) -> Tuple[str, str]:
    """100% offline, deterministic grounded response generator.
    
    Synthesizes facts directly from matching passages without requiring any API keys or network connection.
    Guarantees no hallucination and full adherence to the source text.
    """
    if not retrieved_chunks:
        return (
            "I could not find information about that in the approved UCLan support pages. "
            "For specialized enquiries, please contact the Inclusive Support team at "
            "<a href='mailto:inclusivesupport@uclan.ac.uk'>inclusivesupport@uclan.ac.uk</a>.",
            "STARPath Grounded Fallback"
        )

    best = retrieved_chunks[0]
    content = best.get("content", "").strip()
    title = best.get("page_title", "")
    section = best.get("section", "")
    url = best.get("url", "")
    date_col = best.get("date_collected", "2026-11-12")

    # Split into clean sentences
    sentences = [s.strip() for s in content.split(". ") if s.strip()]
    if not sentences:
        body = content
    elif len(sentences) <= 3:
        body = ". ".join(sentences) + ("." if not sentences[-1].endswith(".") else "")
    else:
        # Prioritize matching sentences
        q_words = set(query.lower().split())
        scored_sents = []
        for s in sentences:
            match_count = sum(1 for w in q_words if len(w) > 3 and w in s.lower())
            scored_sents.append((match_count, s))
        scored_sents.sort(key=lambda x: x[0], reverse=True)
        top_sents = [s for _, s in scored_sents[:3]]
        body = ". ".join(top_sents) + ("." if not top_sents[-1].endswith(".") else "")

    answer = (
        f"{body}\n\n"
        f"*(According to **{title}** — Section: *{section}*)*"
    )
    return answer, "STARPath Grounded Synthesizer (Offline/Local)"


def generate_rag_answer(query: str, retrieved_chunks: List[Dict[str, Any]]) -> Tuple[str, str]:
    """Orchestrates LLM call based on LLM_PROVIDER setting with automatic resilient fallback.
    
    Returns:
        answer_text: Grounded response
        provider_used: Description of provider that produced the answer
    """
    prompt = format_context_prompt(query, retrieved_chunks)

    # 1. Try Google Gemini if configured
    if LLM_PROVIDER == "gemini":
        try:
            return call_gemini_api(prompt)
        except Exception as e:
            logger.warning("Gemini API call failed (%s). Falling back to offline grounded synthesizer.", e)
            answer, _ = offline_grounded_synthesizer(query, retrieved_chunks)
            return (
                f"{answer}\n\n"
                f"> *[Note: The online Gemini service was unavailable; this answer was generated via local grounded fallback.]*",
                "Offline Fallback (Gemini rate-limited/offline)"
            )

    # 2. Try Local Ollama if configured
    if LLM_PROVIDER == "ollama":
        try:
            return call_ollama_api(prompt)
        except Exception as e:
            logger.warning("Ollama call failed (%s). Falling back to offline grounded synthesizer.", e)
            answer, _ = offline_grounded_synthesizer(query, retrieved_chunks)
            return (
                f"{answer}\n\n"
                f"> *[Note: Local Ollama was not responding; this answer was generated via local grounded fallback.]*",
                "Offline Fallback (Ollama unreachable)"
            )

    # 3. Default: Offline Grounded Synthesizer
    return offline_grounded_synthesizer(query, retrieved_chunks)


def simplify_answer_text(text: str) -> str:
    """Rewrite text in very simple, plain English for international students."""
    # Remove complex jargon and shorten sentences
    simplified = text
    replacements = {
        "eligible offer-holders": "accepted students",
        "offer-holders": "students accepted to the university",
        "halls of residence": "student flats on campus",
        "reasonable adjustments": "helpful changes for your study",
        "assistive technology": "helpful computer software and tools",
        "diagnostic assessment": "an official test with a specialist",
        "subsidize": "help pay for",
        "residential": "staying overnight in university rooms",
        "non-repayable": "free money that you do not need to give back",
        "sensory impairments": "hearing or sight differences",
        "neurodiversity": "different ways of thinking like dyslexia or autism",
        "participation in the STAR programme is completely free of charge": "the STAR programme is 100% free"
    }
    for old, new in replacements.items():
        simplified = simplified.replace(old, new).replace(old.capitalize(), new.capitalize())

    return simplified
