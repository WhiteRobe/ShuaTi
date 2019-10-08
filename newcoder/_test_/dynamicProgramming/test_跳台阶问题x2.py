import unittest
from newcoder.dynamicProgramming import 跳台阶 as tT1
from newcoder.dynamicProgramming import 变态跳台阶 as tT2


class TestFunc(unittest.TestCase):
    def test_tiaotaijie1(self):
        s = tT1.Solution()
        self.assertEqual(s.jumpFloor(1), 1)
        self.assertEqual(s.jumpFloor(2), 2)
        self.assertEqual(s.jumpFloor(3), 3)
        self.assertEqual(s.jumpFloor(4), 5)
        self.assertEqual(s.jumpFloor(5), 8)

    def test_tiaotaijie2(self):
        s = tT2.Solution()
        self.assertEqual(s.jumpFloorII(1), 1)
        self.assertEqual(s.jumpFloorII(2), 2)
        self.assertEqual(s.jumpFloorII(3), 4)
        self.assertEqual(s.jumpFloorII(4), 8)
        self.assertEqual(s.jumpFloorII(5), 16)


if __name__ == '__main__':
    unittest.main()