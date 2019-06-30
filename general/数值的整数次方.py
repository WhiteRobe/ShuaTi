"""
题目来源：
    牛客网
    @See https://www.nowcoder.com/practice/1a834e5e3e1a4b7ba251417554e07c00?tpId=13&tqId=11165&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
题目描述
    给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。(求base的exponent次方可以为负)
思路:
    详见下
样例输入:
    2 10
    8 1
    7 0
    2 9
    2 -3
样例输出：
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
        # 如 2^10 = 2^8 * 2^2 变为 0b1010 = 2^0b1000 * 2^0b10 => x << 8 * 2 << 2
        if exponent == 0:
            return 1
        negative, result = exponent < 0, 1
        exponent = abs(exponent)
        while exponent > 0:
            if exponent & 0b1 == 1:
                result *= base
            result *= result
            exponent = exponent >> 1
        return 1.0 / result if negative else result


if __name__ == '__main__':
    s = Solution()
    assert s.Power(2, 10) == 1024
    assert s.Power(8, 1) == 8
    assert s.Power(7, 0) == 1
    assert s.Power(2, 9) == 512
    assert s.Power(2, -3) == 0.125
