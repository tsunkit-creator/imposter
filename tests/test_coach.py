import unittest

from imposter_coach.coach import build_diagnostic_questions, evaluate_answers


class CoachTests(unittest.TestCase):
    def test_build_diagnostic_questions_for_python(self):
        questions = build_diagnostic_questions("python")
        self.assertEqual(len(questions), 3)
        self.assertIn("function", questions[1].lower())

    def test_high_confidence_answers_score_above_threshold(self):
        answers = [
            "In Python, a list stores ordered values, while a dictionary stores key-value pairs for lookup by name.",
            "I would use a function to filter even numbers from a list and return the result.",
            "Mutable default arguments can leak state between calls, so using None is safer and more explicit.",
        ]
        result = evaluate_answers(answers, "python")
        self.assertGreaterEqual(result["score"], 10)
        self.assertIn("classic imposter syndrome", result["summary"].lower())

    def test_low_confidence_answers_score_below_threshold(self):
        answers = [
            "I do not understand it well yet.",
            "I am still learning the basics.",
            "I need more examples before I can explain it.",
        ]
        result = evaluate_answers(answers, "python")
        self.assertLess(result["score"], 10)
        self.assertIn("skill gap", result["summary"].lower())


if __name__ == "__main__":
    unittest.main()
