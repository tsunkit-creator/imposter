from __future__ import annotations

from .coach import Coach, build_diagnostic_questions, evaluate_answers


def main() -> None:
    print("Imposter Coach")
    print("This tool helps assess whether your doubt matches your real capability.\n")

    topic = input("What topic do you feel like an imposter in? ").strip() or "Python"
    self_rating = input("How confident do you feel, from 1 to 10? ").strip() or "5"

    try:
        self_rating_value = int(self_rating)
    except ValueError:
        self_rating_value = 5

    coach = Coach(topic=topic, self_rating=self_rating_value)
    questions = coach.diagnostic_questions()

    print("\nPlease answer these three questions as honestly as you can.\n")
    answers = []
    for index, question in enumerate(questions, start=1):
        print(f"{index}. {question}")
        answer = input("Your answer: ").strip()
        answers.append(answer)
        print()

    result = evaluate_answers(answers, topic)

    print("Assessment")
    print("-" * 40)
    print(f"Topic: {topic}")
    print(f"Self-rated confidence: {self_rating_value}/10")
    print(f"Score: {result['score']}/15")
    print(result["summary"])
    print()
    print("Coaching guidance:")
    print(result["coaching"])


if __name__ == "__main__":
    main()
