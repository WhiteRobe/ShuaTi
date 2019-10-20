import unittest
from leetcode.array import 缀点成线5230 as tT


class MyTestCase(unittest.TestCase):
    def test_true(self):
        s = tT.Solution()
        self.assertTrue(s.checkStraightLine(coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))

    def test_one_point(self):
        s = tT.Solution()
        self.assertTrue(s.checkStraightLine(coordinates=[[1, 2]]))

    def test_two_point(self):
        s = tT.Solution()
        self.assertTrue(s.checkStraightLine(coordinates=[[1, 2], [25, 695]]))

    def test_false(self):
        s = tT.Solution()
        self.assertFalse(s.checkStraightLine(coordinates=[[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))

    def test_horizontal(self):
        s = tT.Solution()
        self.assertTrue(s.checkStraightLine(coordinates=[[1, 1], [2, 1], [3, 1]]))

    def test_vertical(self):
        s = tT.Solution()
        self.assertTrue(s.checkStraightLine(coordinates=[[1, 1], [1, 2], [1, 4], [1, 5], [1, 6], [1, 7]]))


if __name__ == '__main__':
    unittest.main()
