import unittest
from newcoder.linklist import 栈的压入弹出序列 as tT


class MyTestCase(unittest.TestCase):
    def test_true(self):
        s = tT.Solution()
        self.assertTrue(s.IsPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))

    def test_true_2(self):
        s = tT.Solution()
        self.assertTrue(s.IsPopOrder([1, 2, 3, 4, 5], [3, 5, 4, 2, 1]))

    def test_true_3(self):
        s = tT.Solution()
        self.assertTrue(s.IsPopOrder([1], [1]))

    def test_false(self):
        s = tT.Solution()
        self.assertFalse(s.IsPopOrder([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))

    def test_false_2(self):
        s = tT.Solution()
        self.assertFalse(s.IsPopOrder([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))

    def test_not_include(self):
        s = tT.Solution()
        self.assertFalse(s.IsPopOrder([1, 2, 3, 4, 5], [9, 8, 2, 1, 4]))

    def test_empty(self):
        s = tT.Solution()
        self.assertTrue(s.IsPopOrder([], []))


if __name__ == '__main__':
    unittest.main()
