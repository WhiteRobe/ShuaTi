"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/problems/maximum-subarray/
    题目序号 53
题目描述:
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
思路:
    DP(见下) 或者 分治法，时间复杂度理论上分别为 O(n) 和 O(nlogn)
    1. DP: 若之前子序列的和值大于0 说明对nums[i]有增益 则子序列加入nums[i]
        若之前子序列的和值小于0 显然应该丢弃这个序列，重新从nums[i]计数
    2. 分治法: @See https://leetcode-cn.com/problems/maximum-subarray/solution/bao-li-qiu-jie-by-pandawakaka/
样例输入:
    [-2,1,-3,4,-1,2,1,-5,4]
样例输出:
    6
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_v, tmp = nums[0], 0
        for i in nums:
            tmp = tmp + i if tmp > 0 else i
            max_v = max(tmp, max_v)  # 更新全局最大值

        return max_v

    def maxSubArray2(self, nums: List[int]) -> int:
        # 分治法
        # 最大子序和要么在左半边，要么在右半边，要么是穿过中间
        # 不过由于要计算中间序列，实际上时间复杂度要高于DP

        if len(nums) == 1:
            return nums[0]

        # 计算左右最大子序列值
        mid = len(nums) // 2
        max_l = self.maxSubArray2(nums[:mid])
        max_r = self.maxSubArray2(nums[mid:])

        # 计算跨越左右的最大子序列值
        max_ml = self.cal_max(nums[:mid][::-1])
        max_mr = self.cal_max(nums[mid:])

        return max(max_l, max_r, max_ml+max_mr)

    def cal_max(self, nums):
        max_v, tmp = nums[0], 0
        for i in nums:
            tmp += i
            max_v = max(tmp, max_v)
        return max_v
