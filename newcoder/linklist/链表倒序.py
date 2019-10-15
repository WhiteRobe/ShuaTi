"""
题目来源：
    牛客网
    @See https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035
    剑指offer 题16
题目描述
    输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
思路:
    @See https://blog.csdn.net/Shenpibaipao/article/details/72669323
样例输入:
    (1) -> (2) -> (3) -> None # 详见class ListNode
样例输出：
    [3, 2, 1]
"""


# 已知
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        before, head, result = None, None, []
        while listNode:
            before, head = head, listNode  # 前节点和现节点的指针移动
            listNode = listNode.next  # 由于此时head指向listNode，下一行若先执行会替换掉listNode.next为before，因此本行必先执行
            head.next = before
        while head:
            result += [head.val]
            head = head.next
        return result
        # 以上是模仿C语言的写法
        # python可以更简洁
        # if listNode is None:
        #     return []
        # return self.printListFromTailToHead(listNode.next) + [listNode.val]


# if __name__ == '__main__':
#
#     head = ListNode(1)
#     c = head
#     c.next = ListNode(2)
#     c = c.next
#     c.next = ListNode(3)
#     c = None
#
#     assert Solution().printListFromTailToHead(head) == [3, 2, 1]
#     assert Solution().printListFromTailToHead(None) == []
