"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/contest/weekly-contest-160/problems/circular-permutation-in-binary-representation/
    题目序号 周赛160 5239
题目描述:
    给你两个整数 n 和 start。你的任务是返回任意 (0,1,2,,...,2^n-1) 的排列 p，并且满足：
        · p[0] = start
        · p[i] 和 p[i+1] 的二进制表示形式只有一位不同
        · p[0] 和 p[2^n -1] 的二进制表示形式也只有一位不同
思路:
    其实就是格雷码的生成
样例输入:
    n = 2, start = 3
    3, 2
样例输出:
    [3,2,0,1] 或 [3, 1, 0, 2]
        解释：这个排列的二进制表示是 (11,10,00,01) 所有的相邻元素都有一位是不同的，另一个有效的排列是 [3,1,0,2]
    [2, 3, 1, 0, 4, 5, 7, 6] 或 [2, 6, 7, 5, 4, 0, 1, 3]
"""
from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        ret = [start]
        for i in range(n):
            m = len(ret)
            for j in range(m-1, -1, -1):
                ret.append(ret[j] ^ (1 << i))  # 由 第n个格雷码生成第n+1个格雷码 如 11 ^ 01 = 10
        return ret
