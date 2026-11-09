import unittest

from src.training_test import run_training_test, score


class TrainingTestV1Tests(unittest.TestCase):
    def test_all_answers_pass(self):
        result = run_training_test(["first version", "YES"])
        self.assertEqual(result, {"score": 2, "total": 2, "passed": True})

    def test_partial_answers_are_scored(self):
        self.assertEqual(score(["first version", "no"]), 1)

    def test_extra_answers_do_not_change_total(self):
        self.assertEqual(score(["first version", "yes", "extra"]), 2)


if __name__ == "__main__":
    unittest.main()
