import unittest
from leetcode.array import 两数之和1 as tT


class MyTestCase(unittest.TestCase):
    def test_normal(self):
        s = tT.Solution()
        self.assertEqual(s.twoSum(nums=[2, 7, 11, 15], target=9), [0, 1])


if __name__ == '__main__':
    unittest.main()
