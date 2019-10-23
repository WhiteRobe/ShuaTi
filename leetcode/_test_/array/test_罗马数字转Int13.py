import unittest
from leetcode.array import 罗马数字转Int13 as tT


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = tT.Solution()
        data = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
        ans = [3, 4, 9, 58, 1994]
        for d, a in zip(data, ans):
            self.assertEqual(a, s.romanToInt(d))


if __name__ == '__main__':
    unittest.main()
