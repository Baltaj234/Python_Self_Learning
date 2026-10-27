"""Core classes for a small, text-based arithmetic game."""

import random
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class MathQuestion:
    """An arithmetic problem and its answer."""

    left: int
    operator: str
    right: int
    answer: int

    @classmethod
    def generate(
        cls, operation: str, max_number: int, rng: random.Random
    ) -> "MathQuestion":
        if operation not in {"+", "-", "*", "/"}:
            raise ValueError(f"Unsupported operation: {operation}")
        if max_number < 1:
            raise ValueError("max_number must be at least 1")

        if operation == "/":
            right = rng.randint(1, max_number)
            answer = rng.randint(1, max_number)
            left = right * answer
        else:
            left = rng.randint(1, max_number)
            right = rng.randint(1, max_number)
            if operation == "+":
                answer = left + right
            elif operation == "-":
                answer = left - right
            else:
                answer = left * right

        return cls(left, operation, right, answer)

    def __str__(self) -> str:
        return f"{self.left} {self.operator} {self.right}"


@dataclass
class GameStats:
    """Results from one game session."""

    correct: int = 0
    answered: int = 0
    best_streak: int = 0


class MathGame:
    """Runs a game session and reports the player's score."""

    DIFFICULTY_LIMITS = {
        "easy": 10,
        "medium": 25,
        "hard": 100,
    }

    def __init__(
        self,
        rng: random.Random | None = None,
        input_fn: Callable[[str], str] = input,
        output_fn: Callable[[str], None] = print,
    ) -> None:
        self.rng = rng or random.Random()
        self.input = input_fn
        self.output = output_fn

    def play(self, operation: str, difficulty: str, rounds: int) -> GameStats:
        if operation not in {"+", "-", "*", "/", "mixed"}:
            raise ValueError(f"Unsupported operation: {operation}")
        if difficulty not in self.DIFFICULTY_LIMITS:
            raise ValueError(f"Unsupported difficulty: {difficulty}")
        if rounds < 1:
            raise ValueError("rounds must be at least 1")

        max_number = self.DIFFICULTY_LIMITS[difficulty]
        stats = GameStats()
        streak = 0

        self.output(
            f"\nStarting a {difficulty} game with {operation} problems "
            f"for {rounds} rounds!"
        )
        while stats.answered < rounds:
            question_operation = operation
            if operation == "mixed":
                question_operation = self.rng.choice(["+", "-", "*", "/"])
            question = MathQuestion.generate(
                question_operation, max_number, self.rng
            )
            while True:
                response = self.input(f"{question} = (or q to quit): ").strip()
                if response.lower() == "q":
                    self._show_results(stats, rounds)
                    return stats
                try:
                    answer = int(response)
                except ValueError:
                    self.output("Please enter a whole number, or q to quit.")
                    continue
                break

            stats.answered += 1
            if answer == question.answer:
                stats.correct += 1
                streak += 1
                stats.best_streak = max(stats.best_streak, streak)
                self.output("Correct!")
            else:
                streak = 0
                self.output(f"Not quite. The answer is {question.answer}.")

        self._show_results(stats, rounds)
        return stats

    def _show_results(self, stats: GameStats, rounds: int) -> None:
        self.output(
            f"\nGame over! Score: {stats.correct}/{stats.answered} "
            f"(out of {rounds} rounds). Best streak: {stats.best_streak}."
        )
