import unittest
from newcoder.general import 数值的整数次方 as tT


class TestFunc(unittest.TestCase):
    def test_replaceSpace(self):
        s = tT.Solution()
        assert s.Power(0, 0) == 1  # 按C语言库的标准，该值为1
        assert s.Power(0, 7) == 0
        assert s.Power(2, 10) == 1024
        assert s.Power(8, 1) == 8
        assert s.Power(7, 0) == 1
        assert s.Power(2, 9) == 512
        assert s.Power(2, -3) == 0.125


if __name__ == '__main__':
    unittest.main()
