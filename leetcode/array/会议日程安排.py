"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/contest/biweekly-contest-11/problems/meeting-scheduler/
    题目序号 周赛夜场11 5089
题目描述:
    给你两位客户的可用时间间隔 slots1 和 slots2，以及会议的预计持续时间 duration，请你帮他们安排合适的会议时间。

    「会议时间」是指用户都能够参加且持续时间满足预计时间 duration 的 最早的时间间隔 。

    如果没有满足要求的会面时间，就返回一个 空数组 。

    「时间间隔」的格式是 [start, end]，由两个元素 start 和 end 组成，表示从 start 开始，到 end 结束。

    题目保证同一个人的可用时间间隔不会出现交叠的情况，也就是说，
    对于同一个人的两个时间间隔 [start1, end1] 和 [start2, end2]，要么 start1 > end2，要么 start2 > end1。

思路:

样例输入:
    slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
    slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
样例输出:
    [60,68]
    []
数据约定：
    1 <= slots1.length, slots2.length <= 10^4
    slots1[i].length, slots2[i].length == 2
    slots1[i][0] < slots1[i][1]
    slots2[i][0] < slots2[i][1]
    0 <= slots1[i][j], slots2[i][j] <= 10^9
    1 <= duration <= 10^6
"""
from typing import List


class Solution:
    # def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
    # time_line_start, time_line_end = {}, {}
    # slots1 = list(filter(lambda x: x[1] - x[0] >= duration, slots1))
    # slots2 = list(filter(lambda x: x[1] - x[0] >= duration, slots2))
    # for start, end in slots1:
    #     if end - start < duration:
    #         continue
    #     for i in range(start, end+1):  # 这一步太吃时间了
    #         time_line_start[i] = [start, end]
    #         time_line_end[i] = [start, end]
    #
    # for start, end in slots2:
    #     if end - start < duration:
    #         continue
    #     for i in range(start, end):
    #         if i in time_line_start:
    #             if time_line_start[i][0] + duration < min(end, time_line_start[i][1]):
    #                 return [time_line_start[i][0], time_line_start[i][0]+duration]
    #         if i in time_line_end:
    #             if time_line_start[i][1] - duration < max(start, time_line_start[i][0]):
    #                 return [time_line_start[i][1]-duration, time_line_start[i][1]]
    # return []
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # slots1 = list(filter(lambda x: x[1] - x[0] >= duration, slots1))
        # slots2 = list(filter(lambda x: x[1] - x[0] >= duration, slots2))
        time_line_1 = {}
        for start, end in slots1:
            if end - start < duration:
                continue
            time_line_1[start] = (1, end)
            time_line_1[end] = (0, start)

        for start, end in slots2:
            if end - start < duration:
                continue
            for key in range(start, end - duration + 1):
                if key in time_line_1 and time_line_1[key][0] == 1:
                    print(key + duration, end, time_line_1[key][1])
                    if key + duration <= min(end, time_line_1[key][1]):
                        return [key, key + duration]

            for key in range(end, start + duration - 1, -1):
                if key in time_line_1 and time_line_1[key][0] == 0:
                    print(key + duration, end, time_line_1[key][1])
                    if key - duration >= max(start, time_line_1[key][1]):
                        return [key - duration, key]
        return []


if __name__ == '__main__':
    assert [0, 12] == Solution().minAvailableDuration(slots1=[[0, 10000000]], slots2=[[0, 10000000]], duration=12)
    a = [0, 1, 2, 3]
    for i in range(3, 2, -1):
        print(i)
