import unittest
from leetcode.tree import 删除子文件夹 as tT


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        s = tT.Solution()
        self.assertEqual(["/a", "/c/d", "/c/f"], s.removeSubfolders(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))

    def test_case_2(self):
        s = tT.Solution()
        self.assertEqual(["/a"], s.removeSubfolders(folder=["/a", "/a/b/c", "/a/b/d"]))

    def test_case_3(self):
        s = tT.Solution()
        self.assertEqual(["/a/b/c", "/a/b/d", "/a/b/ca"], s.removeSubfolders(folder=["/a/b/c", "/a/b/d", "/a/b/ca"]))

    def test_case_4(self):
        s = tT.Solution()
        self.assertEqual(["/ah/al"], s.removeSubfolders(folder=["/ah/al/am", "/ah/al"]))

    def test_case_5(self):
        s = tT.Solution()
        self.assertEqual(["/ah/al"], s.removeSubfolders(folder=["/ah/al", "/ah/al/am"]))


if __name__ == '__main__':
    unittest.main()
