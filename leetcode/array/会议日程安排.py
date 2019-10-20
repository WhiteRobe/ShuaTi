"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/contest/biweekly-contest-11/problems/meeting-scheduler/
    @See https://leetcode-cn.com/problems/meeting-scheduler/
    题目序号 周赛夜场11 5089
题目描述:
    给你两位客户的可用时间间隔 slots1 和 slots2，以及会议的预计持续时间 duration，请你帮他们安排合适的会议时间。

    「会议时间」是指用户都能够参加且持续时间满足预计时间 duration 的 最早的时间间隔 。

    如果没有满足要求的会面时间，就返回一个 空数组 。

    「时间间隔」的格式是 [start, end]，由两个元素 start 和 end 组成，表示从 start 开始，到 end 结束。

    题目保证同一个人的可用时间间隔不会出现交叠的情况，也就是说，
    对于同一个人的两个时间间隔 [start1, end1] 和 [start2, end2]，要么 start1 > end2，要么 start2 > end1。

思路:
    先排序，然后双指针分别指向两个区间，注意指针的移动即可（根据结束时间来移动）
    @See https://leetcode-cn.com/circle/article/4Zpy7m/
    @See 扫描线算法 https://leetcode-cn.com/tag/line-sweep/
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
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda _: _[0])
        slots2.sort(key=lambda _: _[0])
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            # 当前对比区间为 第一个人的第 i 个区间，第二个人的第 j 的区间
            # 区间开始为两个人开始的最晚值，区间结束为两个人结束的最早值
            start, end = max(slots1[i][0], slots2[j][0]), min(slots1[i][1], slots2[j][1])
            # 重叠区间够会议时间
            if end >= start + duration:
                return [start, start + duration]
            # 谁的结束时间比较早，向后移动一位
            if slots1[i][1] > slots2[j][1]:
                j += 1
            else:
                i += 1
        return []
