"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/problems/3sum/
    题目序号 13
题目描述:
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

    注意：答案中不可以包含重复的三元组。

思路:
    先排序
    给出三个指针：迭代i，L=i+1, R=len(nums)
    若 三者之和 大于0 R--;小于0 L++；等于0加入
    需要注意筛选掉重复项；i指向的值大于0时可以直接跳出迭代循环
样例输入:
    [-1, 0, 1, 2, -1, -4]
样例输出:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:  # 移除重复项
                continue

            L, R = i+1, len(nums)-1
            while L < R:
                L, R, res = self.cal((n, L, R, nums))
                results += res
                # sums = sum([n, nums[L], nums[R]])
                # if sums == 0:
                #     results.append([n, nums[L], nums[R]])
                #     L, R = self.remove_duplicate(L, R, nums)
                # elif sums < 0:
                #     L += 1
                # elif sums > 0:
                #     R -= 1
        return results

    def cal(self, params):
        n, L, R, nums = params
        results, sums = [], sum([n, nums[L], nums[R]])
        if sums == 0:
            results.append([n, nums[L], nums[R]])
            L, R = self.remove_duplicate(L, R, nums)
        elif sums < 0:
            L += 1
        elif sums > 0:
            R -= 1
        return L, R, results

    def remove_duplicate(self, L, R, nums):
        # 过滤重复项
        while L < R and nums[L] == nums[L + 1]:
            L += 1
        while L < R and nums[R] == nums[R - 1]:
            R -= 1
        return L + 1, R - 1




