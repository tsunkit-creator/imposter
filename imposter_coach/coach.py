from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


TOPIC_KEYWORDS = {
    "python": [
        "function",
        "loop",
        "list",
        "dictionary",
        "class",
        "mutable",
        "debug",
        "exception",
        "module",
    ],
    "c#": [
        "class",
        "method",
        "namespace",
        "async",
        "garbage",
        "interface",
        "exception",
        "generic",
        "linq",
    ],
    "javascript": [
        "function",
        "async",
        "closure",
        "scope",
        "object",
        "prototype",
        "event",
        "callback",
        "promise",
    ],
    "sql": [
        "join",
        "index",
        "query",
        "schema",
        "transaction",
        "constraint",
        "aggregate",
        "normalization",
        "where",
    ],
}


@dataclass
class Coach:
    topic: str = ""
    self_rating: int = 5
    answers: List[str] = field(default_factory=list)

    def diagnostic_questions(self) -> List[str]:
        return build_diagnostic_questions(self.topic)

    def evaluate(self) -> dict:
        if not self.answers:
            raise ValueError("No answers provided for evaluation.")
        return evaluate_answers(self.answers, self.topic)


def build_diagnostic_questions(topic: str) -> List[str]:
    normalized = (topic or "software engineering").strip().lower()
    if "python" in normalized:
        return [
            "Explain the difference between a list and a dictionary in Python, and when you would use each.",
            "Write a short function that filters a list of numbers, returns only even values, and explain your logic.",
            "What are the common pitfalls of mutable default arguments or shared state in Python programs?",
        ]
    if "c#" in normalized:
        return [
            "Explain the difference between a class and a record in C#, and when each is appropriate.",
            "Write a short method that iterates a collection, filters by a condition, and transforms the result.",
            "What are the trade-offs between value types, reference types, and nullability in C#?",
        ]
    if "javascript" in normalized:
        return [
            "Explain scope and closures in JavaScript with a brief practical example.",
            "Describe how async/await differs from promises, and when you would choose each.",
            "What are common pitfalls with hoisting, truthiness, and object mutation in JavaScript?",
        ]
    if "sql" in normalized:
        return [
            "Explain how JOINs work and when to prefer INNER JOIN versus LEFT JOIN.",
            "Describe how indexes improve query performance and when they can hurt performance.",
            "What is the difference between a transaction and a single query, and why does isolation matter?",
        ]
    return [
        "Describe the core concepts behind the topic and the main problems it helps solve.",
        "Give an example of how you would apply the topic in a real project.",
        "Explain the most common edge cases or failure modes someone should watch for.",
    ]


def evaluate_answers(answers: List[str], topic: str) -> dict:
    keywords = TOPIC_KEYWORDS.get((topic or "").lower(), TOPIC_KEYWORDS["python"])
    total_score = 0
    per_answer_scores = []

    for answer in answers:
        normalized = answer.lower()
        matches = sum(1 for keyword in keywords if keyword in normalized)
        score = min(5, matches + 1)
        total_score += score
        per_answer_scores.append(score)

    total_score += max(0, 5 - int((topic or "").count(" ")))
    total_score = min(15, total_score)

    if total_score >= 10:
        summary = (
            "Your responses show real capability in this area. The pattern suggests classic imposter syndrome: "
            "you are underrating your actual skill relative to your demonstrated understanding."
        )
        coaching = (
            "Use the evidence in your answers as the basis for confidence. Focus on what you already know and build "
            "from that foundation instead of comparing yourself to stronger peers."
        )
    else:
        summary = (
            "This looks more like a normal skill gap than fraud or a lack of intelligence. You are still early in the learning curve "
            "for this topic, and that is completely normal."
        )
        coaching = (
            "Pick a small, concrete learning path: read the official docs, build a tiny project, and review one concept at a time. "
            "Competence grows from repetition and feedback, not from feeling instantly certain."
        )

    return {
        "score": total_score,
        "breakdown": per_answer_scores,
        "summary": summary,
        "coaching": coaching,
        "topic": topic,
    }
