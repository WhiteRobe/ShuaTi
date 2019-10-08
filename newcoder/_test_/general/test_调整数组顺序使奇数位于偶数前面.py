import unittest
from newcoder.general import 调整数组顺序使奇数位于偶数前面 as tT


class TestFunc(unittest.TestCase):
    def test_replaceSpace(self):
        s = tT.Solution()
        assert s.reOrderArray([1, 2, 3, 4, 5, 6, 7]) == [1, 3, 5, 7, 2, 4, 6]
        assert s.reOrderArray([2, 4, 6, 1, 3, 5, 7]) == [1, 3, 5, 7, 2, 4, 6]


if __name__ == '__main__':
    unittest.main()
