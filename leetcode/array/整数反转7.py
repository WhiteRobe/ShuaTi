"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/problems/reverse-integer/
    题目序号 7
题目描述:
    给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
    假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。
    请根据这个假设，如果反转后整数溢出那么就返回 0。
思路:
    转成字符串直接反转，python牛逼就完事了
样例输入:
    1230
    -123
    0
    1534236469
样例输出:
    321
    -321
    0
    0
"""
import re


class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)[::-1]
        is_negative = -1 if '-' == str_x[-1] else 1
        # 去除无用的0和负号
        str_x = re.sub(r'^0+', '', str_x)
        str_x = re.sub(r'-', '', str_x)
        # 注意是否为0
        x = int(str_x if str_x != '' else 0) * is_negative
        # 溢出判定
        if x < - 2**31 or x > 2 ** 31 -1:
            return 0
        return x

