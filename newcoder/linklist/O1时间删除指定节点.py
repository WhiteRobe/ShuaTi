"""
题目来源:
    剑指offer 面试题13
题目描述:
    给定单向链表的头指针和一个结点指针，在O(1)时间内删除该结点。
思路:
    把target节点的后一个节点复制到target上即可，有两个特例：
        1. 删除尾节点  -> 解决方法在python里我只能想到去遍历 O(n) 但是时间总复杂度为 [(n-1)*O(1) + O(n)]/n
        2. 仅有一个节点(也是尾节点问题) -> 直接置None
        3. 节点不在链表里 -> 大部分情况下没问题，就是非尾节点时要考虑 1. 处遍历时的 while 终止条件
样例输入:

样例输出:

"""


# class LinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def delete(self, head, target):
        next = target.next

        if next is None:
            if head == target:
                head = None
            else:  # O(n)
                c = head
                while c.next and c.next != target:  # 要防止节点不在链表内 `c.next is not None`
                    c = c.next
                c.next = None
        else:
            self.copy_to(next, target)
        return head

    def copy_to(self, from_node, to_node):
        to_node.val = from_node.val
        to_node.next = from_node.next