import unittest

from main import sort_the_people as solution


class TestSolution(unittest.TestCase):

    def test_solution_cases(self):
        cases = [
            (["Mary","John","Emma"], [180,165,170], ["Mary","Emma","John"]),
            (["Alice","Bob","Bob"], [155,185,150], ["Bob","Alice","Bob"]),

            (["Alice"], [155], ["Alice"]),
            (["Bob"], [1], ["Bob"]),
            (["X"], [10**5], ["X"]),

            (["A","B"], [1,2], ["B","A"]),
            (["A","B"], [2,1], ["A","B"]),

            (["A","B","C"], [150,160,170], ["C","B","A"]),

            (["A","B","C"], [170,160,150], ["A","B","C"]),

            (["Bob","Bob","Bob"], [150,160,170], ["Bob","Bob","Bob"]),

            (["A","B"], [1,10**5], ["B","A"]),
            (["A","B"], [10**5,1], ["A","B"]),

            (["A","B","C","D","E"], [150,200,100,180,120], ["B","D","A","E","C"]),

            (["A","B","C","D","E"], [5,4,3,2,1], ["A","B","C","D","E"]),

            (["A","B","C","D","E"], [1,2,3,4,5], ["E","D","C","B","A"]),

            (["Bob","Alice","Bob","Alice"], [180,150,160,170], ["Bob","Alice","Bob","Alice"]),

            ([f"name{i}" for i in range(1000)],
             list(range(1, 1001)),
             [f"name{i}" for i in range(999, -1, -1)]),
        ]
        for names, heights, expected in cases:
            with self.subTest(names=names, heights=heights):
                self.assertEqual(solution(names, heights), expected)


if __name__ == "__main__":
    unittest.main()
