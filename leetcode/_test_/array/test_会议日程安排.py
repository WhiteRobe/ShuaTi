import unittest
from leetcode.array import 会议日程安排 as tT
import time


class MyTestCase(unittest.TestCase):
    def test_meet(self):
        s = tT.Solution()
        self.assertEqual([60, 68],
                         s.minAvailableDuration(slots1=[[10, 50], [60, 120], [140, 210]], slots2=[[0, 15], [60, 70]],
                                                duration=8))

    def test_meet_2(self):
        s = tT.Solution()
        self.assertEqual([1, 2], s.minAvailableDuration(slots1=[[0, 2]], slots2=[[1, 3]], duration=1))

    def test_meet_3(self):
        s = tT.Solution()
        self.assertEqual([100, 1000100],
                         s.minAvailableDuration(slots1=[[0, 1], [100, 1000100]], slots2=[[90, 1000100], [0, 2]],
                                                duration=1000000))

    def test_no_meet(self):
        s = tT.Solution()
        self.assertEqual([],
                         s.minAvailableDuration(slots1=[[10, 50], [60, 120], [140, 210]], slots2=[[0, 15], [60, 70]],
                                                duration=12))

    def test_time_limit(self):
        start = time.time()
        s = tT.Solution()
        self.assertEqual([],
                         s.minAvailableDuration(slots1=[[10, 50], [60, 120], [140, 210]], slots2=[[0, 15], [60, 70]],
                                                duration=12))
        self.assertEqual([0, 12],
                         s.minAvailableDuration(slots1=[[0, 10000000]], slots2=[[0, 10000000]],
                                                duration=12))
        assert time.time() - start < 1000 * 5


if __name__ == '__main__':
    unittest.main()
