import unittest
from leetcode.array import 整数反转7 as tT


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = tT.Solution()
        self.assertEqual(s.reverse(1230), 321)
        self.assertEqual(s.reverse(109000), 901)
        self.assertEqual(s.reverse(-1203), -3021)
        self.assertEqual(s.reverse(0), 0)
        self.assertEqual(s.reverse(1534236469), 0)


if __name__ == '__main__':
    unittest.main()
