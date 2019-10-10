"""
题目来源：
    牛客网
    @See https://www.nowcoder.com/practice/1a834e5e3e1a4b7ba251417554e07c002
题目描述
    给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。(求base的exponent次方可以为负)
思路:
    详见下
样例输入:
    0 0
    0 7
    2 10
    8 1
    7 0
    2 9
    2 -3
样例输出：
    1
    0
    1024
    8
    1
    512
    0.125
"""

import math
class Solution:
    def Power(self, base, exponent):
        # write code here
        # 1. 直接调用API。 别问，问就是python牛逼
        # return math.pow(base, exponent)
        # 2. O(nlogn)的算法，采用切分的递归调用
        # if exponent == 0:
        #     return 1
        # elif exponent == 1:
        #     return base
        # elif exponent == -1:
        #     return 1.0 / base
        # # a^n = a^n/2 * a^n/2 (n为偶数)
        # # a^n = a^(n-1)/2 * a^(n-1)/2 * a (n为奇数)
        # partition = self.Power(base, exponent >> 1)  # 用 ">>1" 替代 "// 2"
        # partition *= partition
        # if exponent & 0b1 == 1:  # 用 "& 0b1" 替代 "%2"
        #     return partition * base
        # return partition
        # 3. 事实上还可以采用二进制分解指数的方式求解
        # 如 3^7 = 3^4 * 3^1 变为 0b101 = 3^0b100 * 3^0b1 = 3^4 * 3^1
        negative, result = exponent < 0, 1
        exponent = abs(exponent)
        while exponent > 0:
            if exponent & 0b1 == 1:
                result *= base  # 累加
            base *= base  # 该位所代表的值向上升一倍 (2的指数，每进位一次，即每次翻倍)
            exponent = exponent >> 1
        return 1.0 / result if negative else result

