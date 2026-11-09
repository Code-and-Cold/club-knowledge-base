import unittest

from main import flip_the_pancakes as solution


class TestSolution(unittest.TestCase):

    def test_solution_cases(self):
        cases = [
            ([3,2,4,1], None),
            ([1,2,3], None),

            ([1], []),

            ([1,2], []),
            ([2,1], [2]),

            ([1,2,3,4,5], []),
            ([1,2,3,4,5,6,7,8,9,10], []),

            ([2,1], [2]),
            ([3,2,1], [3]),
            ([5,4,3,2,1], None),

            ([5,1,2,3,4], None),
            ([3,1,2], None),

            ([1,2,3,4,5], []),
            ([2,3,4,5,1], None),

            ([3,1,2], None),
            ([1,3,2], None),
            ([2,3,1], None),
            ([4,2,1,3], None),
            ([3,2,4,1], None),

            ([1,2], []),
            ([2,1], [2]),

            (list(range(100, 0, -1)), None),
            (list(range(1, 101)), []),
        ]

        for arr, expected in cases:
            with self.subTest(arr=arr):
                result = solution(list(arr))  # копия, т.к. решение может мутировать
                if expected is not None:
                    self.assertEqual(result, expected)
                else:
                    self._assert_valid_pancake_result(arr, result)

    def _assert_valid_pancake_result(self, arr, flips):
        """Проверяет, что последовательность flips действительно сортирует arr,
        и что каждый flip корректен (1 <= k <= n)."""
        n = len(arr)
        a = list(arr)
        for k in flips:
            self.assertGreaterEqual(k, 1)
            self.assertLessEqual(k, n)
            a[:k] = reversed(a[:k])
        self.assertEqual(a, list(range(1, n + 1)))


if __name__ == "__main__":
    unittest.main()
