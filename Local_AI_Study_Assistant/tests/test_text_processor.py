import pytest

from text_processor import TextProcessor


def test_prepare_text_removes_extra_whitespace() -> None:
    processor = TextProcessor()
    text = "   Python\n is   easy\t to learn.   "

    cleaned = processor.prepare_text(text)

    assert cleaned == "Python is easy to learn."


def test_summarize_returns_short_summary() -> None:
    processor = TextProcessor()
    text = (
        "Python is a popular programming language. "
        "It is used for automation, data science, and web development. "
        "Many beginners start with Python because it is easy to read."
    )

    summary = processor.summarize(text)

    assert "Summary:" in summary
    assert "Python is a popular programming language." in summary


def test_build_prompt_rejects_empty_text() -> None:
    processor = TextProcessor()

    with pytest.raises(ValueError):
        processor.build_summary_prompt("   ")

    with pytest.raises(ValueError):
        processor.build_question_prompt("\n")

    with pytest.raises(ValueError):
        processor.build_explanation_prompt("")


def test_split_sentences_handles_basic_cases() -> None:
    processor = TextProcessor()
    text = "Python is simple. Learning it is fun. It works for scripts."

    sentences = processor.split_sentences(text)

    assert len(sentences) == 3
    assert sentences[0] == "Python is simple."
    assert sentences[-1] == "It works for scripts."


def test_summarize_empty_text_raises_error() -> None:
    processor = TextProcessor()

    with pytest.raises(ValueError):
        processor.summarize("   ")
