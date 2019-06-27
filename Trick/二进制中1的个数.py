"""
题目来源：
    牛客网
    @See https://www.nowcoder.com/practice/8ee967e43c2c4ec193b040ea7fbb10b8?tpId=13&tqId=11164&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
题目描述：
    输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
思路:
    对于一个正数，操作：n = (n - 1) & n 将经过 k 次把 n 变为0；
    对于一个负数，将其 n & 0xffffffff (C中int:32位即4字节长) 可以将该负数转为补码表示的负数。(python 语言限定，因为python无Overflow)
样例输入:
    9
    -1
样例输出：
    2
    32
"""


# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count, n = 0, n & 0xffffffff  # 强制负数取补码（取C语言中一个int的大端32位，即四字节），等价于
        # count, n = 0, n if n >= 0 else 4294967296 + n  # 这么做是因为 python 的语言特性
        while n > 0:
            count += 1
            n = (n - 1) & n
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1(-1))
    # print(9, bin(9))
    # print(-1, bin(-1), bin(-1 & 0xffffffff))
    # print(-0b010, bin(-0b010 & 0b1111), -0b010 & 0b1111)
