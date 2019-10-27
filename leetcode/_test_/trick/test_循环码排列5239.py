import unittest
from leetcode.trick import 循环码排列5239 as tT


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = tT.Solution()
        res = s.circularPermutation(2, 3)
        assert res == [3, 2, 0, 1] or res == [3, 1, 0, 2]

    def test_something_2(self):
        s = tT.Solution()
        res = s.circularPermutation(3, 2)
        assert [2, 3, 1, 0, 4, 5, 7, 6] == res or res == [2, 6, 7, 5, 4, 0, 1, 3]


if __name__ == '__main__':
    unittest.main()
