from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List


class ConversationHistory:
    """Store Q&A pairs for the current application session."""

    def __init__(self) -> None:
        self._entries: List[Dict[str, Any]] = []

    def add(self, question: str, answer: str) -> None:
        """Add a question and answer to the conversation history."""
        clean_question = question.strip()
        clean_answer = answer.strip()

        if not clean_question:
            raise ValueError("Question cannot be empty.")
        if not clean_answer:
            raise ValueError("Answer cannot be empty.")

        self._entries.append(
            {
                "question": clean_question,
                "answer": clean_answer,
                "timestamp": datetime.now().isoformat(timespec="seconds"),
            }
        )

    def get_recent(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Return the most recent entries, newest last in the list."""
        if limit <= 0:
            return []
        return list(self._entries[-limit:])

    def is_empty(self) -> bool:
        return len(self._entries) == 0

    def clear(self) -> None:
        self._entries.clear()

    def __len__(self) -> int:
        return len(self._entries)
