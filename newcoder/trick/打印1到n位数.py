"""
题目来源:
    剑指Offer 面试题12 p94(纪念版)
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
        self.results = []

    def func(self, n):
        self.len = n
        self.num = ['0' for _ in range(n)]
        self.recursive(0)
        return [x for x in self.results if x is not None]

    def recursive(self, index):
        if index == self.len:
            return self.output()

        for i in range(0, 10):
            self.num[index] = str(i)
            self.results.append(self.recursive(index+1))

    def output(self):
        from re import sub
        num = sub(r'^0+', '', ''.join(self.num))
        return '0' if num == '' else num


if __name__ == '__main__':
    s = MySolution()
    results = s.func(2)
    print(results)
