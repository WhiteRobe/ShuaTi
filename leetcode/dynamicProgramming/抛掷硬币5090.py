"""
题目来源:
    Leetcode
    @See https://leetcode-cn.com/contest/biweekly-contest-11/problems/toss-strange-coins/
    @See https://leetcode-cn.com/problems/toss-strange-coins/
    题目序号 周赛夜场11 5090
题目描述:
    有一些不规则的硬币。在这些硬币中，prob[i] 表示第 i 枚硬币正面朝上的概率。

    请对每一枚硬币抛掷 一次，然后返回正面朝上的硬币数等于 target 的概率。
思路:
    动态规划 res[x]指的是恰好x个为正的概率
    @See 动态规划 https://leetcode-cn.com/tag/dynamic-programming/
样例输入:
    prob = [0.4], target = 1
    prob = [0.5,0.5,0.5,0.5,0.5], target = 0
样例输出:
    0.4000
    0.03125

数值提示：
    1 <= prob.length <= 1000
    0 <= prob[i] <= 1
    0 <= target <= prob.length
    如果答案与标准答案的误差在 10^-5 内，则被视为正确答案。
"""
from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        res = [0 for _ in range(len(prob) + 1)]
        res[0] = 1.0
        for i in range(1, len(prob)+1):
            for j in range(min(i, target), -1, -1):
                # 恰好j个为正 = 上一轮更新中j个正面的情况下第i个恰好为反 + 已经j-1个正面的情况下第i个继续为正
                res[j] = res[j] * (1 - prob[i - 1]) + (res[j - 1] * prob[i - 1] if j > 0 else 0)

        return res[target]
