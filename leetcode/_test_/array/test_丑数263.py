import unittest
from leetcode.array import 丑数263 as tT


class MyTestCase(unittest.TestCase):
    def test_one(self):
        s = tT.Solution()
        self.assertEqual(True, s.isUgly(1))

    def test_cases(self):
        s = tT.Solution()
        is_ug = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36]
        for i in range(1, 20):
            self.assertEqual(i in is_ug, s.isUgly(i))


if __name__ == '__main__':
    unittest.main()
