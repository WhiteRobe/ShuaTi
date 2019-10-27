import unittest
from leetcode.array import 串联字符串的最大长度5240 as tT


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = tT.Solution()
        self.assertEqual(4, s.maxLength(["un", "iq", "ue"]))

    def test_case2(self):
        s = tT.Solution()
        self.assertEqual(6, s.maxLength(["cha", "r", "act", "ers"]))

    def test_case3(self):
        s = tT.Solution()
        self.assertEqual(5, s.maxLength(["a", "b", "c", "d", "e", 'ed']))
        self.assertEqual(6, s.maxLength(["a", "b", "c", "d", "e", 'f']))

    def test_one_list_element(self):
        s = tT.Solution()
        self.assertEqual(2, s.maxLength(["un"]))
        self.assertEqual(9, s.maxLength(["unewrplij"]))

    def test_empty(self):
        s = tT.Solution()
        self.assertEqual(0, s.maxLength([]))

    def test_duplicate(self):
        s = tT.Solution()
        self.assertEqual(0, s.maxLength(["unupol"]))
        self.assertEqual(2, s.maxLength(["un", "ue"]))


if __name__ == '__main__':
    unittest.main()
