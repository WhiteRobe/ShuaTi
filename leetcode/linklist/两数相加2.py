"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/problems/add-two-numbers/
    题目序号 2
题目描述:
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
思路:
    注意代码的鲁棒性即可，要防止 5 + 5 这种只算到 5 而忘了进位的情况
样例输入:
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
样例输出:
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
"""
from structure.list_node import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head, carry = ListNode(None), 0  # 哑节点和进位指示器
        current = head
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sums = l1_val + l2_val + carry

            carry = int(sums >= 10)
            new_node = ListNode(sums % 10)

            current.next = new_node

            current, l1, l2 = current.next, self.safe_next(l1), self.safe_next(l2)

        return head.next

    def safe_next(self, l):
        return l.next if l else l
