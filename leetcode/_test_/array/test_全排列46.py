import unittest
from leetcode.array import 全排列46 as tT


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = tT.Solution()
        ans = s.permute(nums=[1, 2, 3])
        self.assertEqual([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]].sort(), ans.sort())

    def test_case2(self):
        s = tT.Solution()
        ans = s.permute(nums=[1, 2])
        self.assertEqual([[2, 1], [1, 2]].sort(), ans.sort())

    def test_one(self):
        s = tT.Solution()
        ans = s.permute(nums=[1])
        self.assertEqual([[1]].sort(), ans.sort())

    def test_empty(self):
        s = tT.Solution()
        ans = s.permute(nums=[])
        self.assertEqual([[]].sort(), ans.sort())


if __name__ == '__main__':
    unittest.main()
