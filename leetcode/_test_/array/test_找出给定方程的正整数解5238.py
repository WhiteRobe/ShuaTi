import unittest
from leetcode.array import 找出给定方程的正整数解5238 as tT


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = tT.Solution()
        self.assertEqual([[1, 4], [2, 3], [3, 2], [4, 1]].sort(), s.findSolution(tT.CustomFunction(), 5).sort())

    def test_no_answer(self):
        s = tT.Solution()
        self.assertEqual([], s.findSolution(tT.CustomFunction(), -1))

    def test_duplicate_answer(self):
        s = tT.Solution()
        self.assertEqual([[1, 5], [2, 4], [3, 3], [4, 2], [5, 1]].sort(), s.findSolution(tT.CustomFunction(), 6).sort())


if __name__ == '__main__':
    unittest.main()
