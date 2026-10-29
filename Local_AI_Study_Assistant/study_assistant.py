from __future__ import annotations

from typing import Optional

from ai_model import LocalAIModel, ModelNotAvailableError
from conversation_history import ConversationHistory
from text_processor import TextProcessor


class StudyAssistant:
    """Coordinate the application's features and interact with the model."""

    def __init__(
        self,
        model: LocalAIModel,
        conversation_history: Optional[ConversationHistory] = None,
        text_processor: Optional[TextProcessor] = None,
    ) -> None:
        self.model = model
        self.history = conversation_history or ConversationHistory()
        self.text_processor = text_processor or TextProcessor()

    def ask_question(self, question: str) -> str:
        """Send a direct question to the local model."""
        cleaned_question = self.text_processor.prepare_text(question)
        if not cleaned_question:
            raise ValueError("Please enter a question before asking the AI.")

        prompt = self.text_processor.build_question_prompt(cleaned_question)
        answer = self.model.generate(prompt)
        self.history.add(cleaned_question, answer)
        return answer

    def summarize_text(self, text: str) -> str:
        """Send a text block to the model for a summary."""
        cleaned_text = self.text_processor.prepare_text(text)
        if not cleaned_text:
            raise ValueError("Please enter text to summarize.")

        prompt = self.text_processor.build_summary_prompt(cleaned_text)
        answer = self.model.generate(prompt)
        self.history.add(f"Summary request: {cleaned_text[:80]}", answer)
        return answer

    def explain_concept(self, concept: str) -> str:
        """Ask the model to explain a technical topic in beginner-friendly terms."""
        cleaned_concept = self.text_processor.prepare_text(concept)
        if not cleaned_concept:
            raise ValueError("Please enter a technical concept to explain.")

        prompt = self.text_processor.build_explanation_prompt(cleaned_concept)
        answer = self.model.generate(prompt)
        self.history.add(f"Explain concept: {cleaned_concept}", answer)
        return answer

    def show_history(self, limit: int = 5) -> str:
        """Return recent Q&A pairs with the newest entries at the end."""
        if self.history.is_empty():
            return "No recent questions yet. Start by asking your first question."

        entries = self.history.get_recent(limit)
        output_lines = []
        for index, entry in enumerate(entries, start=1):
            output_lines.append(f"{index}. Question: {entry['question']}")
            output_lines.append(f"   Answer: {entry['answer']}")
        return "\n".join(output_lines)

    def clear_history(self) -> None:
        self.history.clear()

    def check_model_status(self) -> str:
        if self.model.is_available():
            return "The local model is ready."
        return (
            "The local model is not ready. Start Ollama first, then run "
            "'ollama pull llama3.2:3b'."
        )

    def safe_generate(self, prompt: str) -> str:
        """Wrapper for model calls that may fail due to missing runtime support."""
        try:
            return self.model.generate(prompt)
        except ModelNotAvailableError:
            raise
