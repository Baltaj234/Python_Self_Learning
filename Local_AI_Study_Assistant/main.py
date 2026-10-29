from __future__ import annotations

from ai_model import LocalAIModel, ModelNotAvailableError, ModelRequestError
from study_assistant import StudyAssistant


MODEL_NAME = "llama3.2:3b"


def read_multiline_input(prompt_message: str) -> str:
    """Collect a multi-line text block until an empty line ends it."""
    print(prompt_message)
    lines: list[str] = []

    while True:
        try:
            line = input()
        except EOFError:
            break

        if line.strip() == "" and lines:
            break

        lines.append(line)

    return "\n".join(lines).strip()


def print_menu() -> None:
    print("\n=== Local AI Study Assistant ===")
    print("1. Ask a question")
    print("2. Summarize text")
    print("3. Explain a concept")
    print("4. View recent conversation")
    print("5. Exit")


def run_app() -> None:
    model = LocalAIModel(model_name=MODEL_NAME)
    assistant = StudyAssistant(model=model)

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip().lower()

        if choice in {"5", "exit", "quit", "q"}:
            print("Goodbye! Thanks for studying with the local AI assistant.")
            break

        try:
            if choice == "1":
                question = input("Ask your question: ").strip()
                if not question:
                    print("Please enter a question before continuing.")
                    continue
                answer = assistant.ask_question(question)
                print("\nAI response:\n" + answer)

            elif choice == "2":
                text = read_multiline_input("Paste or type the text to summarize. Press Enter on a blank line to finish.")
                if not text:
                    print("Please enter some text before summarizing.")
                    continue
                answer = assistant.summarize_text(text)
                print("\nAI summary:\n" + answer)

            elif choice == "3":
                concept = input("Enter a technical concept to explain in simple language: ").strip()
                if not concept:
                    print("Please enter a concept before continuing.")
                    continue
                answer = assistant.explain_concept(concept)
                print("\nAI explanation:\n" + answer)

            elif choice == "4":
                print("\nRecent conversation:")
                print(assistant.show_history())

            else:
                print("Please choose a valid option from 1 to 5.")

        except ModelNotAvailableError as exc:
            print(f"\nModel error: {exc}")
            print("Quick fix: open a new terminal and run:")
            print("  ollama serve")
            print(f"  ollama pull {MODEL_NAME}")
            retry = input("Press Enter to try again or type 'exit' to leave: ").strip().lower()
            if retry == "exit":
                print("Exiting the application.")
                break
        except ModelRequestError as exc:
            print(f"\nThe model responded with a request error: {exc}")
        except ValueError as exc:
            print(f"\nInput error: {exc}")
        except Exception as exc:  # pragma: no cover - safety net for unexpected runtime errors.
            print(f"\nUnexpected error: {exc}")


if __name__ == "__main__":
    run_app()
