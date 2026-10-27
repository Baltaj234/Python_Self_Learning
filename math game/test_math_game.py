import random
import unittest

from math_game import MathGame, MathQuestion


class MathQuestionTests(unittest.TestCase):
    def test_generated_question_answers_match_each_operation(self):
        for operation in ("+", "-", "*", "/"):
            with self.subTest(operation=operation):
                question = MathQuestion.generate(operation, 10, random.Random(2))
                if operation == "+":
                    expected = question.left + question.right
                elif operation == "-":
                    expected = question.left - question.right
                elif operation == "*":
                    expected = question.left * question.right
                else:
                    expected = question.left // question.right
                    self.assertEqual(question.left % question.right, 0)
                self.assertEqual(question.answer, expected)

    def test_rejects_unknown_operation(self):
        with self.assertRaises(ValueError):
            MathQuestion.generate("%", 10, random.Random(1))


class MathGameTests(unittest.TestCase):
    def test_invalid_input_does_not_consume_a_round(self):
        expected = MathQuestion.generate("+", 10, random.Random(5)).answer
        responses = iter(("not a number", str(expected), "q"))
        messages = []
        game = MathGame(
            rng=random.Random(5),
            input_fn=lambda _prompt: next(responses),
            output_fn=messages.append,
        )

        stats = game.play("+", "easy", 2)

        self.assertEqual(stats.answered, 1)
        self.assertEqual(stats.correct, 1)
        self.assertTrue(any("whole number" in message for message in messages))
        self.assertEqual(stats.best_streak, 1)


if __name__ == "__main__":
    unittest.main()
