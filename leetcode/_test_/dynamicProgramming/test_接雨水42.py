import unittest
from leetcode.dynamicProgramming import 接雨水42 as tT


class MyTestCase(unittest.TestCase):
    def test_normal_case(self):
        s = tT.Solution()
        self.assertEqual(6, s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    def test_normal_case2(self):
        s = tT.Solution()
        self.assertEqual(1, s.trap([0, 1, 0, 1, 0]))

    def test_normal_case23(self):
        s = tT.Solution()
        self.assertEqual(1, s.trap([4, 2, 3]))

    def test_empty(self):
        s = tT.Solution()
        self.assertEqual(0, s.trap([0, 1, 0]))

    def test_null(self):
        s = tT.Solution()
        self.assertEqual(0, s.trap([]))
        self.assertEqual(0, s.trap([0]))
        self.assertEqual(0, s.trap([1]))


if __name__ == '__main__':
    unittest.main()
