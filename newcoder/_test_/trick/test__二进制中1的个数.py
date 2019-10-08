import unittest
from newcoder.trick import 二进制中1的个数 as tT


class TestFunc(unittest.TestCase):
    def test_replaceSpace(self):
        s = tT.Solution()
        assert s.NumberOf1(9) == 2
        assert s.NumberOf1(-1) == 32


if __name__ == '__main__':
    unittest.main()
