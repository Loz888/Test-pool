"""Local-only regression tests for the synthetic sample."""

import unittest

from sample import total_points


class TotalPointsTests(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(total_points([]), 0)

    def test_positive_points(self):
        self.assertEqual(total_points([1, 2, 3]), 6)

    def test_zero_and_negative_points(self):
        self.assertEqual(total_points([8, 0, -3]), 5)

    def test_generator_input(self):
        self.assertEqual(total_points(n for n in range(4)), 6)

    def test_large_integers(self):
        self.assertEqual(total_points([10**30, 10**30]), 2 * 10**30)

    def test_rejects_non_integer_values(self):
        for value in (True, False, 1.5, "2", None):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    total_points([1, value])


if __name__ == "__main__":
    unittest.main()
