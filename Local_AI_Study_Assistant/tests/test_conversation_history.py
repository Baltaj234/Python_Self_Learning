from conversation_history import ConversationHistory


def test_add_single_conversation() -> None:
    history = ConversationHistory()

    history.add("What is Python?", "Python is a beginner-friendly programming language.")

    assert len(history) == 1
    assert history.get_recent(1)[0]["question"] == "What is Python?"
    assert history.get_recent(1)[0]["answer"] == "Python is a beginner-friendly programming language."


def test_empty_history() -> None:
    history = ConversationHistory()

    assert history.is_empty() is True
    assert history.get_recent(5) == []
    assert len(history) == 0


def test_add_multiple_entries_and_retrieve_most_recent() -> None:
    history = ConversationHistory()

    history.add("First question", "First answer")
    history.add("Second question", "Second answer")
    history.add("Third question", "Third answer")

    recent = history.get_recent(2)

    assert len(recent) == 2
    assert recent[0]["question"] == "Second question"
    assert recent[1]["question"] == "Third question"


def test_history_rejects_empty_values() -> None:
    history = ConversationHistory()

    try:
        history.add("", "Answer")
        assert False, "Expected ValueError for an empty question."
    except ValueError:
        pass

    try:
        history.add("Question", "")
        assert False, "Expected ValueError for an empty answer."
    except ValueError:
        pass
