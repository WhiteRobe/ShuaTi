"""
题目来源：
    牛客网
    @See https://www.nowcoder.com/practice/72a5a919508a4251859fb2cfb987a0e6
    题目序号
题目描述
    我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
思路:
    归纳发现是 斐波那契数列数列
    @See https://uploadfiles.nowcoder.com/images/20170718/3614591_1500381257269_B18DB55610F4CC5E67C96674FE51EBDC
    需要注意的是，递归容易暴栈
样例输入:
    0
    1
    2
    3
    4
    5
样例输出：
    0
    1
    2
    3
    5
    8
"""


class Solution:
    def rectCover(self, number):
        history, n = [0, 1, 2], number
        for i in range(3, number+1):
            temp = history[2]
            history[2] = sum(history)
            history[1] = temp

        return history[min(number, 2)]

    def rectCover_r(self, number):
        # 递归版本容易爆栈
        return number if number < 3 else self.rectCover(number - 1) + self.rectCover(number - 2)
