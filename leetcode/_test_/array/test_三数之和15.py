import unittest
from leetcode.array import 三数之和15 as tT


class MyTestCase(unittest.TestCase):
    def test_normal(self):
        s = tT.Solution()
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], s.threeSum([-1, -1, 0, 1, 2, -1, -4]))

    def test_duplicate(self):
        s = tT.Solution()
        self.assertEqual([[-2, 1, 1]], s.threeSum([-2, -2, 1, 1, 1, 1, 1, 1, 1, 1]))

    def test_empty_input(self):
        s = tT.Solution()
        self.assertEqual([], s.threeSum([]))

    def test_empty_output(self):
        s = tT.Solution()
        self.assertEqual([], s.threeSum([9, 1, 2, 3]))
        self.assertEqual([], s.threeSum([-1, 7, 0, 8, 10]))


if __name__ == '__main__':
    unittest.main()
