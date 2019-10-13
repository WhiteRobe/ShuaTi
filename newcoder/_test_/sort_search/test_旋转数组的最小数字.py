import unittest
from newcoder.sort_search import 旋转数组的最小数字 as tT


class MyTestCase(unittest.TestCase):
    def test_empty_input(self):
        s = tT.Solution()
        self.assertEqual(0, s.minNumberInRotateArray([]))

    def test_order_input(self):
        s = tT.Solution()
        self.assertEqual(1, s.minNumberInRotateArray([1, 3, 5, 9, 10]))
        self.assertEqual(1, s.minNumberInRotateArray([1, 3, 3, 9, 10]))

    def test_equal_input1(self):
        s = tT.Solution()
        self.assertEqual(0, s.minNumberInRotateArray([2, 3, 0, 2, 2, 2, 2]))

    def test_equal_input2(self):
        s = tT.Solution()
        self.assertEqual(0, s.minNumberInRotateArray([2, 2, 2, 2, 0, 1, 2]))

    def test_normal_input(self):
        s = tT.Solution()
        self.assertEqual(1, s.minNumberInRotateArray([5, 7, 7, 9, 1, 2, 4]))
        self.assertEqual(1, s.minNumberInRotateArray([5, 7, 7, 9, 1, 1, 2, 4]))
        self.assertEqual(1, s.minNumberInRotateArray([3, 4, 5, 1, 2]))
        self.assertEqual(0, s.minNumberInRotateArray([2, 3, 0, 1, 2, 2, 2]))

    def test_2_input(self):
        s = tT.Solution()
        self.assertEqual(0, s.minNumberInRotateArray([0, 1]))
        self.assertEqual(0, s.minNumberInRotateArray([1, 0]))


if __name__ == '__main__':
    unittest.main()
