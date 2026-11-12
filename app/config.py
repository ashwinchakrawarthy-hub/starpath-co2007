"""Configuration settings for STARPath."""
import os
from pathlib import Path
from dotenv import load_dotenv

# Base directory paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Load .env file if present
load_dotenv(BASE_DIR / ".env")

# Language Model Configuration
# Available options: "offline" (zero-dependency local), "gemini" (Google Gemini API), "ollama" (Local Ollama)
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "offline").lower().strip()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash").strip()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate").strip()
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2").strip()

# Retrieval parameters
TOP_K_CHUNKS = int(os.getenv("TOP_K_CHUNKS", "3"))
SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", "0.18"))

# Web Application Settings
APP_NAME = "STARPath"
APP_SUBTITLE = "Accessible STAR Programme Assistant"
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))

# File paths
CHUNKS_PATH = DATA_DIR / "chunks.json"
GLOSSARY_PATH = DATA_DIR / "glossary.json"
SOURCES_PATH = DATA_DIR / "sources.csv"
MANIFEST_PATH = DATA_DIR / "manifest.json"
EVAL_QUESTIONS_PATH = DATA_DIR / "eval_questions.csv"
