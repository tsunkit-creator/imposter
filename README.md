# Imposter Coach

This project is a lightweight, deterministic coaching app for imposter syndrome. It does not use an agentic LLM workflow. Instead, it asks about a topic, poses three technical questions, scores the answers, and explains whether the user is likely experiencing genuine imposter syndrome or simply needs a clearer learning baseline.

## What it does

- Asks for the topic and a self-rated confidence level
- Gives three topic-specific diagnostic questions
- Scores answers against a simple rubric
- Produces a balanced coaching response based on evidence

## Run it in VS Code

1. Open the folder in VS Code.
2. Open a terminal in the workspace.
3. Create a virtual environment:
   `python -m venv .venv`
4. Activate it:
   - Windows PowerShell: `.venv\Scripts\Activate.ps1`
   - Command Prompt: `.venv\Scripts\activate.bat`
5. Start the app:
   `python -m imposter_coach.main`

## Project structure

- `imposter_coach/` — application code
- `tests/` — validation tests
- `pyproject.toml` — Python project metadata

## Notes

This is intentionally simple and deterministic so the behavior is explainable and repeatable. It is a good foundation if you later want to add a web UI, a richer rubric, or a C# version.
