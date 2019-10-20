import unittest
from leetcode.array import 等差数列中缺失的数字5088 as tT


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = tT.Solution()
        assert s.missingNumber([5, 7, 11, 13]) == 9
        assert s.missingNumber([15, 13, 12]) == 14
        assert s.missingNumber([100, 300, 400]) == 200

    def test_no_miss(self):
        s = tT.Solution()
        assert s.missingNumber([0, 0, 0, 0]) == 0


if __name__ == '__main__':
    unittest.main()
