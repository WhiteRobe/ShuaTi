import unittest
from newcoder.array import 最小K个数 as tT


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = tT.Solution()
        self.assertEqual([2, 3, 4], sorted(s.GetLeastNumbers_Solution([5, 6, 2, 5, 4, 5, 8, 9, 5, 8, 6, 3], 3)))

    def test_can_not_find_k(self):
        s = tT.Solution()
        self.assertEqual([], sorted(s.GetLeastNumbers_Solution([5, 6, 2, 5, 4, 5, 8, 9, 5, 8, 6, 3], 1000)))


if __name__ == '__main__':
    unittest.main()
