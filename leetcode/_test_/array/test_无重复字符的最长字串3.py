import unittest
from leetcode.array import 无重复字符的最长字串3 as tT


class MyTestCase(unittest.TestCase):
    def test_cases(self):
        s = tT.Solution()
        self.assertEqual(s.lengthOfLongestSubstring('abcabcbb'), 3)
        self.assertEqual(s.lengthOfLongestSubstring('bbbbb'), 1)
        self.assertEqual(s.lengthOfLongestSubstring('pwwkew'), 3)
        self.assertEqual(s.lengthOfLongestSubstring('bbba'), 2)

    def test_symmetry(self):
        s = tT.Solution()
        self.assertEqual(s.lengthOfLongestSubstring('abba'), 2)
        self.assertEqual(s.lengthOfLongestSubstring('aba'), 2)
        self.assertEqual(s.lengthOfLongestSubstring('aaabbbaaa'), 2)

    def test_no_repeat(self):
        s = tT.Solution()
        self.assertEqual(s.lengthOfLongestSubstring(' q'), 2)
        self.assertEqual(s.lengthOfLongestSubstring(' '), 1)
        self.assertEqual(s.lengthOfLongestSubstring('z'), 1)
        self.assertEqual(s.lengthOfLongestSubstring('abcdefg'), 7)

    def test_empty(self):
        s = tT.Solution()
        self.assertEqual(s.lengthOfLongestSubstring(''), 0)


if __name__ == '__main__':
    unittest.main()
