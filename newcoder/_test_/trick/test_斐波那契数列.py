import unittest
from newcoder.trick import 斐波那契数列 as tT


class TestFunc(unittest.TestCase):
    def test_replaceSpace(self):
        s = tT.Solution()
        self.assertEqual(s.fibonacci(0), 0)
        self.assertEqual(s.fibonacci(1), 1)
        self.assertEqual(s.fibonacci(2), 1)
        self.assertEqual(s.fibonacci(3), 2)
        self.assertEqual(s.fibonacci(4), 3)
        self.assertEqual(s.fibonacci(5), 5)


if __name__ == '__main__':
    unittest.main()
