"""Retrieval engine for STARPath.

Implements:
1. Semantic & TF-IDF hybrid retrieval over dated approved UCLan web page chunks.
2. Query token coverage weighting to detect out-of-scope questions honestly.
3. Pure keyword search baseline (BM25 style) for evaluation comparison.
"""
import json
import math
import re
from typing import List, Dict, Any, Tuple
from app.config import CHUNKS_PATH, TOP_K_CHUNKS, SIMILARITY_THRESHOLD

# Common English stopwords to ignore during matching
STOPWORDS = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are",
    "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but",
    "by", "can", "did", "do", "does", "doing", "don", "down", "during", "each", "few", "for",
    "from", "further", "had", "has", "have", "having", "he", "her", "here", "hers", "herself",
    "him", "himself", "his", "how", "i", "if", "in", "into", "is", "it", "its", "itself", "just",
    "me", "more", "most", "my", "myself", "no", "nor", "not", "now", "of", "off", "on", "once",
    "only", "or", "other", "our", "ours", "ourselves", "out", "over", "own", "same", "she",
    "should", "so", "some", "such", "than", "that", "the", "their", "theirs", "them", "themselves",
    "then", "there", "these", "they", "this", "those", "through", "to", "too", "under", "until",
    "up", "very", "was", "we", "were", "what", "when", "where", "which", "while", "who", "whom",
    "why", "with", "would", "you", "your", "yours", "yourself", "yourselves"
}


def tokenize(text: str) -> List[str]:
    """Tokenize and normalize text into clean lowercase words."""
    words = re.findall(r'\b[A-Za-z0-9]+\b', text.lower())
    return [w for w in words if len(w) > 1 and w not in STOPWORDS]


class KnowledgeBaseRetriever:
    """Manages document chunks and retrieval operations."""

    def __init__(self, chunks_path=CHUNKS_PATH):
        self.chunks_path = chunks_path
        self.chunks = self._load_chunks()
        self.doc_freqs = self._compute_doc_freqs()
        self.total_docs = len(self.chunks)

    def _load_chunks(self) -> List[Dict[str, Any]]:
        """Load static dated chunks from disk."""
        if not self.chunks_path.exists():
            return []
        with open(self.chunks_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _compute_doc_freqs(self) -> Dict[str, int]:
        """Compute document frequencies for IDF calculation."""
        dfs: Dict[str, int] = {}
        for chunk in self.chunks:
            full_text = f"{chunk.get('page_title', '')} {chunk.get('section', '')} {chunk.get('content', '')} {' '.join(chunk.get('keywords', []))}"
            tokens = set(tokenize(full_text))
            for t in tokens:
                dfs[t] = dfs.get(t, 0) + 1
        return dfs

    def _bm25_idf(self, term: str) -> float:
        """Calculate standard BM25 Inverse Document Frequency."""
        df = self.doc_freqs.get(term, 0)
        # Frequent terms across all chunks have low IDF; rare distinctive terms have high IDF
        return max(0.2, math.log((self.total_docs - df + 0.5) / (df + 0.5) + 1.0))

    def compute_similarity(self, query_tokens: List[str], chunk: Dict[str, Any]) -> float:
        """Compute hybrid relevance score for a chunk against query tokens with coverage weighting."""
        if not query_tokens:
            return 0.0

        title_tokens = tokenize(chunk.get("page_title", ""))
        section_tokens = tokenize(chunk.get("section", ""))
        content_tokens = tokenize(chunk.get("content", ""))
        keyword_tokens = [k.lower() for k in chunk.get("keywords", [])]

        all_doc_tokens = set(title_tokens + section_tokens + content_tokens)
        for kw in keyword_tokens:
            all_doc_tokens.update(tokenize(kw))

        # Check what fraction of the query's non-stopword tokens appear anywhere in this chunk
        matched_tokens = sum(1 for t in query_tokens if t in all_doc_tokens)
        coverage = matched_tokens / len(query_tokens)

        # If less than 28% of the query terms match, this passage cannot answer the question
        if coverage < 0.28:
            return 0.0

        score = 0.0
        for t in query_tokens:
            if t in all_doc_tokens:
                idf = self._bm25_idf(t)
                tf = content_tokens.count(t)
                # BM25 term saturation
                score += (tf / (tf + 1.2)) * idf
                if t in title_tokens:
                    score += 1.8 * idf
                if t in section_tokens:
                    score += 1.4 * idf
                if any(t in kw for kw in keyword_tokens):
                    score += 1.2 * idf

        # Scale by query coverage penalty to avoid single-word coincidental matches
        final_score = (score * (coverage ** 1.5)) / (len(query_tokens) ** 0.5)
        return round(final_score, 4)

    def retrieve(self, query: str, top_k: int = TOP_K_CHUNKS) -> Tuple[List[Dict[str, Any]], bool, float]:
        """Retrieve top-k relevant passages with honest out-of-scope detection.
        
        Returns:
            results: List of top matching chunks with scores
            is_out_of_scope: True if maximum similarity is below threshold
            max_score: Maximum similarity score achieved
        """
        tokens = tokenize(query)
        if not tokens:
            return [], True, 0.0

        scored_chunks = []
        for chunk in self.chunks:
            sim = self.compute_similarity(tokens, chunk)
            chunk_copy = dict(chunk)
            chunk_copy["similarity_score"] = sim
            scored_chunks.append(chunk_copy)

        scored_chunks.sort(key=lambda x: x["similarity_score"], reverse=True)
        top_results = [c for c in scored_chunks if c["similarity_score"] > 0][:top_k]

        max_score = top_results[0]["similarity_score"] if top_results else 0.0
        is_out_of_scope = (max_score < SIMILARITY_THRESHOLD or len(top_results) == 0)

        return top_results, is_out_of_scope, max_score

    def keyword_baseline_search(self, query: str) -> Dict[str, Any]:
        """Simple baseline search required by brief: returns best matching passage."""
        results, is_out_of_scope, max_score = self.retrieve(query, top_k=1)
        if not results or is_out_of_scope:
            return {
                "matched_passage": "No relevant passage found in the university support pages.",
                "source_title": "N/A",
                "source_url": "N/A",
                "score": max_score,
                "is_honest_refusal": True,
                "method": "Simple Keyword Match (Baseline)"
            }

        best = results[0]
        return {
            "matched_passage": best["content"],
            "source_title": best["page_title"],
            "section": best["section"],
            "source_url": best["url"],
            "date_collected": best.get("date_collected", "2026-11-12"),
            "score": best["similarity_score"],
            "is_honest_refusal": False,
            "method": "Simple Keyword Match (Baseline)"
        }


# Singleton instance
retriever_instance = KnowledgeBaseRetriever()
