import unittest
from newcoder.trick import 顺时针打印矩阵 as tT


class MyTestCase(unittest.TestCase):
    def test_normal(self):
        s = tT.Solution()
        self.assertEqual(s.printMatrix([[1, 2, 3],
                                        [4, 5, 6],
                                        [7, 8, 9],
                                        [10, 11, 12]], should_print=False),
                         [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8])

    def test_normal_square(self):
        s = tT.Solution()
        self.assertEqual(s.printMatrix([[1, 2, 3, 4],
                                        [5, 6, 7, 8],
                                        [9, 10, 11, 12],
                                        [13, 14, 15, 16]], should_print=False),
                         [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])

    def test_empty(self):
        s = tT.Solution()
        self.assertEqual(s.printMatrix([[]], should_print=True), [])

    def test_one_row(self):
        s = tT.Solution()
        self.assertEqual(s.printMatrix([[1, 2, 3, 4]], should_print=False), [1, 2, 3, 4])

    def test_one_col(self):
        s = tT.Solution()
        self.assertEqual(s.printMatrix([[1], [2], [3]], should_print=False), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
