"""
题目来源:
    牛客网
    @See https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca
    剑指offer 面试题16
题目描述:
    输入一个链表，反转链表后，输出新链表的表头。
思路:
    倒序链表： @See https://blog.csdn.net/Shenpibaipao/article/details/72669323

样例输入:
    [1 2 3 4 5]
样例输出:
    [5 4 3 2 1]
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        before, head = None, None

        while pHead:
            before, head = head, pHead  # 前节点和现节点的指针移动
            pHead = pHead.next  # 由于此时head指向listNode，下一行若先执行会替换掉listNode.next为before，因此本行必先执行
            head.next = before

        return head