"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/problems/trapping-rain-water/
    题目序号 42
题目描述:
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
思路:
    这题可以直接暴力扫： 对每个位置同时向左右扫描找最低的柱子
    或者可以DP： 1. 从左往右扫，找当前柱子往后所能cover到的水平线；右边同理；2. 两个水平线的交集即为解集。(见下文)
    利用栈 @See https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode/
样例输入:
    [0,1,0,2,1,0,1,3,2,1,2,1]
样例输出:
    6
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        if sum(height) > 1:
            # 计算左右扫描的解集(单侧扫描)
            # left_level, right_level = self.scan_level(height), self.scan_level(height[::-1], reverse=True)
            for i, j in zip(self.scan_level(height), self.scan_level(height, reverse=True)):
                ans += min(i, j)  # 取交集
        return ans

    def scan_level(self, height, reverse=False):
        height = height[::-1] if reverse else height
        level = [0] * len(height)
        current_height = height[0]
        for i, h in enumerate(height):
            level[i] = max(current_height - h, 0)  # 计算所能盛的水量
            current_height = max(h, current_height)  # 修正单侧高度
        return level[::-1] if reverse else level
