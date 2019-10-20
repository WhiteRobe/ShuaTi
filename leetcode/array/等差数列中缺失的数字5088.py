"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/contest/biweekly-contest-11/problems/missing-number-in-arithmetic-progression/
    题目序号 周赛夜场11 5088
题目描述:
    数组 arr 中的值符合等差数列的数值规律：在 0 <= i < arr.length - 1 的前提下，arr[i+1] - arr[i] 的值都相等。

    然后，我们从数组中删去一个 既不是第一个也不是最后一个的值 。

    给你一个缺失值的数组，请你帮忙找出那个被删去的数字。
思路:
    获取前后等差然后逐个比对，等差取绝对值最小的那个
    需要注意负等差和0等差的情况
    ---
    或者直接求和然后按等差数列求和公式做差值运算
样例输入:
    [5,7,11,13]
    [15,13,12]
样例输出:
    9
    14
"""
from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        a, b = arr[0] - arr[1], arr[len(arr) - 2] - arr[len(arr) - 1]
        d = min(abs(a), abs(b))
        d = -d if a < 0 else d
        for i in range(len(arr) - 1):
            if arr[i] - arr[i + 1] != d:
                # print(arr[i] - d)
                return arr[i] - d
        return arr[0]
