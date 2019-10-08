"""
题目来源：
    牛客网
    @See https://www.nowcoder.com/practice/529d3ae5a407492994ad2a246518148a?tpId=13&tqId=11167&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
题目描述
    输入一个链表，输出该链表中倒数第k个结点。
思路:
    给定一个指针，指向当前指针curr往后k个位置的节点。需要注意的是越界的问题。
样例输入:
    {1,2,3,4,5}, 0
    {1,2,3,4,5}, 1
    {1,2,3,4,5}, 2
    {1,2,3,4,5}, 3
    {1,2,3,4,5}, 4
    {1,2,3,4,5}, 5
    {1,2,3,4,5}, 6
样例输出：
    None
    {5}
    {4}
    {3}
    {2}
    {1}
    None
"""


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        k_left, curr = head, head
        for i in range(k):
            if curr is None:
                return None
            curr = curr.next
        while curr:
            curr = curr.next
            k_left = k_left.next
        return k_left


# def get_data():
#     # 准备数据
#     n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
#     head = n1
#     head.next, n2.next, n3.next, n4.next = n2, n3, n4, n5
#     return head


# if __name__ == '__main__':
#     head = get_data()
#
#     s = Solution()
#     assert s.FindKthToTail(head, 0) is None
#     assert s.FindKthToTail(head, 1).val == 5
#     assert s.FindKthToTail(head, 2).val == 4
#     assert s.FindKthToTail(head, 3).val == 3
#     assert s.FindKthToTail(head, 4).val == 2
#     assert s.FindKthToTail(head, 5).val == 1
#     assert s.FindKthToTail(head, 6) is None
