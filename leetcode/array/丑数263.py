"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/problems/ugly-number/
    题目序号  163
题目描述:
    编写一个程序判断给定的数是否为丑数。

    丑数就是只包含质因数 2, 3, 5 的正整数。
思路:
    除以 2 3 5直到除不动为止
    判断剩下的值是否为1，当且仅当为1时为丑数
样例输入:
    1
    8
    14
样例输出:
    true
    true
    false
"""


class Solution:
    def isUgly(self, num: int) -> bool:
        x = 1
        while x != num:  # 没有发生任何值的变动说明已经到底了
            x = num
            for i in [2, 3, 5]:
                num = self.safe_devide(num, i)  # 直接除以2 3 5即可
        return num == 1

    def safe_devide(self, num, dividend):
        return num if num % dividend else num // dividend
