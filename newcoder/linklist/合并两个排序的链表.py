"""
题目来源:
    牛客网
    @See https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337
    剑指offer 面试题17
题目描述:
    输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
思路:
    考虑两种情况：
        ①： 允许使用额外的空间
        ②： 不允许使用额外的空间
    要注意的是代码的健壮性，及传入的两个链表存在空链表的样例。
样例输入:
    [1, 3, 5, 7, 9]
    [2, 4, 6, 8, 10]
样例输出:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        nodes = {0: pHead1, 1: pHead2}

        head, current = None, None
        while nodes[0] or nodes[1]:
            small_one, index = self.choose_smaller_one(nodes[0], nodes[1])
            if head is None:
                head = small_one
                current = head

            nodes[index] = nodes[index].next

            current.next = small_one
            current = current.next

            if self.deal_remain(current, nodes):
                break

        return head

    def choose_smaller_one(self, n1, n2):
        try:
            return (n1, 0) if n1.val < n2.val else (n2, 1)
        except Exception:
            return (n1, 0) if n1 else (n2, 1)

    def deal_remain(self, current, nodes):
        if nodes[0] is None:
            current.next = nodes[1]
        elif nodes[1] is None:
            current.next = nodes[0]
        return not (nodes[0] and nodes[1])
