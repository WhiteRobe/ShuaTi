import unittest
from leetcode.dynamicProgramming import 最大子序和53 as tT


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = tT.Solution()
        self.assertEqual(6, s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    def test_case2(self):
        s = tT.Solution()
        self.assertEqual(-1, s.maxSubArray([-2, -4, -3, -1, -1, -5, -55, -5, -7]))

    def test_case3(self):
        s = tT.Solution()
        self.assertEqual(10, s.maxSubArray([1, 2, 3, 4, -1]))

    def test_one_element(self):
        s = tT.Solution()
        self.assertEqual(-5, s.maxSubArray([-5]))

    def test_case1_d(self):
        s = tT.Solution()
        self.assertEqual(6, s.maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    def test_case2_d(self):
        s = tT.Solution()
        self.assertEqual(-1, s.maxSubArray2([-2, -4, -3, -1, -1, -5, -55, -5, -7]))

    def test_case3_d(self):
        s = tT.Solution()
        self.assertEqual(10, s.maxSubArray2([1, 2, 3, 4, -1]))

    def test_one_element_d(self):
        s = tT.Solution()
        self.assertEqual(-5, s.maxSubArray2([-5]))


if __name__ == '__main__':
    unittest.main()
