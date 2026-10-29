# Local AI Study Assistant

This project is a beginner-friendly command-line application that connects Python to a local Small Language Model (SLM) through Ollama. It lets you ask questions, summarize text, explain technical ideas, and review your recent conversation history without using any paid API or cloud service.

## What this project does

The app helps you learn both Python and local AI integration by showing a clean object-oriented design:

- Ask a question and get an AI response.
- Paste or type a text block and request a summary.
- Ask for a simple explanation of a technical concept.
- Review recent questions and answers from the current session.
- Exit safely when you are done.

This project keeps the design simple and easy to follow for beginners. It is intentionally small but still uses a real, local language model.

## What is an SLM?

A Small Language Model (SLM) is a language model with fewer parameters than a very large foundation model. It is not a toy or a fake response generator; it is an actual pretrained model that runs locally on your computer.

Compared with larger models, SLMs usually:

- use less memory
- run more easily on laptops and desktops
- respond faster in some situations
- have fewer advanced reasoning capabilities
- work well for lightweight tasks and learning projects

For this project, we use a small instruction-tuned model that is realistic for a Windows 11 laptop with an Intel Core i7 and 16 GB RAM.

## Model choice and why it fits

This project uses the Ollama model:

- llama3.2:3b

Why it is a good choice:

- It is a lightweight, CPU-friendly model.
- It is small enough to run on a typical local machine without a dedicated GPU.
- It is instruction-tuned, which means it responds well to natural prompts.
- It is realistic for learning how local AI works without needing paid services.

This makes it appropriate for the hardware described in the project requirements: Windows 11, Intel Core i7, 16 GB RAM, no dedicated GPU.

## How the Python app connects to the model

The application does not use a cloud API. Instead, it talks to a local server started by Ollama.

The Python code sends an HTTP request to:

- http://localhost:11434/api/generate

The request includes:

- the chosen model name
- the prompt text
- a simple JSON payload

Ollama runs the model locally and sends the generated text back to Python. That makes the project simple, practical, and beginner-friendly.

## Project files and classes

Inside the project directory, the code is split into clear files:

- `main.py` - the command-line interface and user menu
- `ai_model.py` - `LocalAIModel` class that talks to Ollama
- `study_assistant.py` - `StudyAssistant` class that manages the app features
- `conversation_history.py` - `ConversationHistory` class that stores Q&A entries
- `text_processor.py` - `TextProcessor` class that cleans text and builds prompts
- `tests/test_conversation_history.py` - tests for conversation history
- `tests/test_text_processor.py` - tests for text processing
- `requirements.txt` - Python dependency information for testing
- `.gitignore` - ignore files created by Python and the virtual environment

### Class responsibilities

#### `LocalAIModel`

This class connects to the local Ollama service. It checks whether the server is running, sends prompts, and handles common errors such as:

- Ollama not running
- model not installed
- empty input
- server connection problems

#### `StudyAssistant`

This class coordinates the program. It does not do all the work itself; instead, it uses the other objects:

- it asks the model for answers
- it stores conversations in `ConversationHistory`
- it uses `TextProcessor` to prepare and format prompts

This separation keeps the program easier to understand and test.

#### `ConversationHistory`

This object stores the current session's questions and answers. It is simple and beginner-friendly, and it demonstrates OOP encapsulation by hiding the internal list of entries behind methods like `add()` and `get_recent()`.

#### `TextProcessor`

This object prepares text before sending it to the model. It removes extra whitespace, splits text into sentences, and builds prompts for questions, summaries, and explanations.

## Prerequisites for Windows 11

Before running the project, make sure the following are installed:

1. Python 3.11 or 3.12
2. VS Code
3. Ollama for Windows
4. A terminal available in VS Code

## Install and start the model runtime

Use the VS Code Terminal and run these commands from the project folder:

```powershell
cd "C:\Users\balta\OneDrive\Desktop\projects\Python_Self_Learning\Local_AI_Study_Assistant"
py -3.12 -m venv .venv
. .\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Then install Ollama from the official website:

- https://ollama.com/download/windows

After installation, open a new terminal and start Ollama:

```powershell
ollama serve
```

In a second terminal, download the model used by this project:

```powershell
ollama pull llama3.2:3b
```

Once the model is installed, run the app from the project directory:

```powershell
python main.py
```

## Run the tests

From the project directory, with the virtual environment active:

```powershell
python -m pytest -q
```

This project uses pytest for the automated tests that do not require an internet connection or a running model.

## Example usage

When the app starts, it shows a menu:

1. Ask a question
2. Summarize text
3. Explain a concept
4. View recent conversation
5. Exit

Example questions:

- What is a variable in Python?
- What is the difference between a list and a tuple?
- How does a function work in Python?

Example summary input:

```text
Python is a general-purpose programming language. It is often used for automation, web development, and data analysis. Many beginners like Python because it is easy to read and write.
```

Example concept explanation:

```text
object-oriented programming
```

## Common errors and troubleshooting

### Ollama is not running

You may see a message saying the local model runtime is unavailable.

Fix it:

```powershell
ollama serve
```

Then try again.

### Model not installed

If the model is missing, you will see a message telling you to run:

```powershell
ollama pull llama3.2:3b
```

### Permission or Python issues on Windows

If Python cannot run the virtual environment or install packages, use the Python Launcher and a project-local virtual environment:

```powershell
py -3.12 -m venv .venv
. .\.venv\Scripts\Activate.ps1
```

### VS Code terminal choice

Use the integrated VS Code terminal, not a separate PowerShell instance outside the project. Run the commands from the project directory so Python can import the project files correctly.

## Limitations of local AI

Local AI is useful, but it has limits:

- It may produce incorrect answers.
- It can be slower than a cloud model, especially on older laptops.
- It uses RAM and CPU resources.
- It may not match the quality of large models.
- It can still be limited by model size and prompt length.

This is normal for a small local model. The goal of this project is to learn how local AI integration works in practice, not to create a perfect AI system.

## What to expect from this project

This project is designed to teach:

- how to create a structured Python project
- how classes interact with each other
- how to write beginner-friendly object-oriented code
- how to use a local SLM with a simple HTTP interface
- how to test parts of an application without depending on AI models

The final result should be a working educational project that is clean, understandable, and realistic for a learner working on a standard Windows 11 laptop.
