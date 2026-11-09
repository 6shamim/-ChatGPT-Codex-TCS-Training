"""A minimal deterministic test harness for Codex training exercises."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    prompt: str
    expected: str


QUESTIONS = (
    Question("What does V1 mean in this project?", "first version"),
    Question("Should a coding agent verify generated files?", "yes"),
)


def score(answers: list[str]) -> int:
    """Return the number of answers matching the expected normalized values."""
    return sum(
        answer.strip().casefold() == question.expected.casefold()
        for answer, question in zip(answers, QUESTIONS)
    )


def run_training_test(answers: list[str]) -> dict[str, int | bool]:
    """Evaluate answers and return a compact, JSON-friendly result."""
    points = score(answers)
    return {
        "score": points,
        "total": len(QUESTIONS),
        "passed": points == len(QUESTIONS),
    }
