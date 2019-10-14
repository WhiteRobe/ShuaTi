"""
题目来源:
    剑指Offer 面试题22 p95(纪念版)
题目描述:
    打印从1到n位数的所有数字
思路:
    数字全排列
样例输入:
    2
样例输出:
    1 2 3 4 5 6 ...  97 98 99
"""


class MySolution:
    def __init__(self):
        self.len = None
        self.num = None

    def func(self, n):
        self.len = n
        self.num = ['0' for _ in range(n)]
        self.recursive(0)

    def recursive(self, index):
        if index == self.len:
            return self.output()

        for i in range(0, 10):
            self.num[index] = str(i)
            self.recursive(index+1)

    def output(self):
        from re import sub
        print(sub(r'^0+', '', ''.join(self.num)))


if __name__ == '__main__':
    s = MySolution()
    s.func(2)
