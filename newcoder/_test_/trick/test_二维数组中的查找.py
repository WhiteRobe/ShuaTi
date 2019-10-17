import unittest
from newcoder.trick import 二维数组中的查找 as tT


class TestFunc(unittest.TestCase):
    def test_find(self):
        s = tT.Solution()
        self.assertTrue(s.Find(6, [[1, 2, 3], [5, 6, 10], [7, 9, 11], [8, 10, 12]]))
        self.assertTrue(s.Find(6, [[1, 5, 7, 8], [2, 6, 9, 10], [3, 10, 11, 12]]))
        self.assertFalse(s.Find(7, [[]]))
        self.assertFalse(s.Find(7, [[1, 2, 3], [4, 6, 8], [11, 12, 13]]))


if __name__ == '__main__':
    unittest.main()
