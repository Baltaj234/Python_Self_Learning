from __future__ import annotations

import re
from typing import List


class TextProcessor:
    """Prepare text and build prompts for the local language model."""

    @staticmethod
    def prepare_text(text: str) -> str:
        value = text or ""
        return re.sub(r"\s+", " ", value.strip())

    @staticmethod
    def split_sentences(text: str) -> List[str]:
        cleaned = TextProcessor.prepare_text(text)
        if not cleaned:
            return []
        sentences = re.split(r"(?<=[.!?])\s+", cleaned)
        return [sentence.strip() for sentence in sentences if sentence.strip()]

    def summarize(self, text: str, max_sentences: int = 3) -> str:
        """Return a simple summary as a short bullet list."""
        sentences = self.split_sentences(text)
        if not sentences:
            raise ValueError("Cannot summarize empty text.")

        selected = sentences[:max_sentences]
        return "Summary:\n- " + "\n- ".join(selected)

    def build_summary_prompt(self, text: str) -> str:
        cleaned = self.prepare_text(text)
        if not cleaned:
            raise ValueError("Text cannot be empty.")
        return (
            "Please summarize the following text in clear, beginner-friendly language. "
            "Keep the summary concise and useful.\n\n"
            f"{cleaned}"
        )

    def build_question_prompt(self, question: str) -> str:
        cleaned = self.prepare_text(question)
        if not cleaned:
            raise ValueError("Question cannot be empty.")
        return (
            "Answer the user's question clearly and helpfully. "
            "Explain the idea in simple English when needed.\n\n"
            f"{cleaned}"
        )

    def build_explanation_prompt(self, concept: str) -> str:
        cleaned = self.prepare_text(concept)
        if not cleaned:
            raise ValueError("Concept cannot be empty.")
        return (
            "Explain the following technical concept in simple, beginner-friendly language. "
            "Use clear examples when helpful.\n\n"
            f"{cleaned}"
        )
