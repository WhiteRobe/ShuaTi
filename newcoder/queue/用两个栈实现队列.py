"""
题目来源:
    牛客网
    @See https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6
题目描述:
    用两个栈来实现一个队列，完成队列的Push/appendTail和Pop/deleteHead操作。 队列中的元素为int类型。
思路:
    栈：  先进后出
    队列：先进先出

    总体思路 ： set 栈A、B，把A栈中的所有弹出到栈B中，则间接实现先进先出；
    (压入) 检查栈B是否为空，非空则把其pop到A，然后A再push/appendTail
    (弹出) 检查栈A是否为空，非空则把其pop到B，然后B再pop/deleteHead
样例输入:

样例输出:

"""


class Stack:
    class Node:
        def __init__(self, node):
            self.val = node
            # self.next = None
            self.prev = None

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, node):
        n = self.Node(node)
        n.prev = self.top
        self.top = n
        self.size += 1

    def pop(self):
        popout = self.top
        self.top = popout.prev if popout is not None else None
        self.size = max(0, self.size-1)
        return popout.val

    def clean(self):
        self.top = None
        self.size = 0

    def empty(self):
        return self.size == 0

    def pop_to(self, stack):
        while self.size > 0:
            stack.push(self.pop())


class Solution:
    def __init__(self):
        self.sa = Stack()
        self.sb = Stack()

    def push(self, node):
        self.append_tail(node)

    def pop(self):
        return self.delete_head()

    def append_tail(self, node):
        if self.sb.size > 0:
            self.sb.pop_to(self.sa)

        self.sa.push(node)

    def delete_head(self):
        if self.sa.size > 0:
            self.sa.pop_to(self.sb)

        return self.sb.pop()
