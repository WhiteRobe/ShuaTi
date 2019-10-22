import unittest
from newcoder.trick import 矩阵覆盖 as tT


class MyTestCase(unittest.TestCase):
    def test_begin(self):
        s = tT.Solution()
        self.assertEqual(s.rectCover(0), 0)
        self.assertEqual(s.rectCover(1), 1)
        self.assertEqual(s.rectCover(2), 2)

    def test_normal(self):
        s = tT.Solution()
        self.assertEqual(s.rectCover(3), 3)
        self.assertEqual(s.rectCover(4), 5)
        self.assertEqual(s.rectCover(5), 8)

    def test_begin_r(self):
        s = tT.Solution()
        self.assertEqual(s.rectCover_r(0), 0)
        self.assertEqual(s.rectCover_r(1), 1)
        self.assertEqual(s.rectCover_r(2), 2)

    def test_normal_r(self):
        s = tT.Solution()
        self.assertEqual(s.rectCover_r(3), 3)
        self.assertEqual(s.rectCover_r(4), 5)
        self.assertEqual(s.rectCover_r(5), 8)


if __name__ == '__main__':
    unittest.main()
