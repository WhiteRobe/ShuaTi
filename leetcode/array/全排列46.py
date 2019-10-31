"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/problems/permutations/
    题目序号 46
题目描述:
    给定一个没有重复数字的序列，返回其所有可能的全排列。
思路:
    1. 回溯算法 @See https://baike.baidu.com/item/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95/9258495
        @See https://leetcode-cn.com/problems/permutations/solution/quan-pai-lie-by-leetcode/
    2. python 库函数
        import itertools
        # return list(itertools.permutations(nums))
        return list(map(lambda x: list(x), itertools.permutations(nums)))
样例输入:
    [1,2,3]
样例输出:
    [[1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]]
"""
from typing import List


class Solution:
    def backtrack(self, nums, tmp, res):
        if not nums:
            res.append(tmp)
            return
        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]], res)

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, [], res)
        return res