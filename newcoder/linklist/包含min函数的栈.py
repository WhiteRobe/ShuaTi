"""
题目来源:
    牛客网
    @See https://www.nowcoder.com/practice/4c776177d2c04c2494f2555c9fcc1e49
    题目序号 剑指offer 21
题目描述:
    定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））
思路:
    创建一个辅助栈，压入一个新值时，比较其和辅助栈栈顶的值，压入二者中较小的值。
        如:依次压入 5243，则辅助栈为： 5 2 2 2 (->栈顶)
    弹出时二者同时弹出
样例输入:
    ["PSH3","MIN","PSH4","MIN","PSH2","MIN","PSH3","MIN","POP","MIN","POP","MIN","POP","MIN","PSH0","MIN"]
样例输出:
    33222330
"""
from structure.stack import ListStack as Stack


class Solution:
    def __init__(self):
        self.main_s = Stack()
        self.min_s = Stack()

    def push(self, node):

        if self.main_s.size() > 0:
            self.min_s.push(min(node, self.min_s.top()))
        else:
            self.min_s.push(node)
        self.main_s.push(node)

    def pop(self):
        self.min_s.pop()
        return self.main_s.pop()

    def top(self):
        return self.main_s.top()

    def min(self):
        return self.min_s.top()
