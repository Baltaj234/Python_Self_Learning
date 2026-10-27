"""Command-line entry point for the math game."""

from math_game import MathGame


def choose_operation() -> str | None:
    choices = {
        "+": "+",
        "add": "+",
        "-": "-",
        "subtract": "-",
        "*": "*",
        "multiply": "*",
        "/": "/",
        "divide": "/",
        "mixed": "mixed",
    }
    while True:
        selection = input(
            "\nChoose an operation: +, -, *, /, or mixed (q to quit): "
        ).strip().lower()
        if selection == "q":
            return None
        if selection in choices:
            return choices[selection]
        print("Please choose +, -, *, /, or mixed.")


def choose_difficulty() -> str:
    while True:
        difficulty = input("Choose difficulty (easy, medium, hard): ").strip().lower()
        if difficulty in MathGame.DIFFICULTY_LIMITS:
            return difficulty
        print("Please choose easy, medium, or hard.")


def choose_rounds() -> int:
    while True:
        selection = input("How many rounds would you like to play? ").strip()
        try:
            rounds = int(selection)
        except ValueError:
            print("Please enter a positive whole number.")
            continue
        if rounds > 0:
            return rounds
        print("Please enter a positive whole number.")


def main() -> None:
    game = MathGame()
    print("Welcome to the Math Game!")
    while True:
        operation = choose_operation()
        if operation is None:
            print("Thanks for playing!")
            return

        difficulty = choose_difficulty()
        rounds = choose_rounds()
        game.play(operation, difficulty, rounds)

        if input("\nPlay again? (y/n): ").strip().lower() not in {"y", "yes"}:
            print("Thanks for playing!")
            return


if __name__ == "__main__":
    main()
