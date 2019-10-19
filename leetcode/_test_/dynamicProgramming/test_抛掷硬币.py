import unittest
from leetcode.dynamicProgramming import 抛掷硬币 as tT


class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        s = tT.Solution()
        self.assertAlmostEqual(0.03125, s.probabilityOfHeads(prob=[0.5, 0.5, 0.5, 0.5, 0.5], target=0), delta=1e-5)

    def test_something_2(self):
        s = tT.Solution()
        self.assertAlmostEqual(0.40000, s.probabilityOfHeads(prob=[0.4], target=1), delta=1e-5)


if __name__ == '__main__':
    unittest.main()
