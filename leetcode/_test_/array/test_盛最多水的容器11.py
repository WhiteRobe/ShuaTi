import unittest
from leetcode.array import 盛最多水的容器11 as tT


class MyTestCase(unittest.TestCase):
    def test_empty(self):
        s = tT.Solution()
        self.assertEqual(0, s.maxArea([1000, 0]))

    def test_case1(self):
        s = tT.Solution()
        self.assertEqual(49, s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))


if __name__ == '__main__':
    unittest.main()
