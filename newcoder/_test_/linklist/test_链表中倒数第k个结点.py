import unittest
from newcoder.linklist import 链表中倒数第k个结点 as tT


def get_data():
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    # 准备数据
    n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    head = n1
    head.next, n2.next, n3.next, n4.next = n2, n3, n4, n5
    return head


class TestFunc(unittest.TestCase):
    def test_replaceSpace(self):
        head = get_data()

        s = tT.Solution()
        assert s.FindKthToTail(head, 0) is None
        assert s.FindKthToTail(head, 1).val == 5
        assert s.FindKthToTail(head, 2).val == 4
        assert s.FindKthToTail(head, 3).val == 3
        assert s.FindKthToTail(head, 4).val == 2
        assert s.FindKthToTail(head, 5).val == 1
        assert s.FindKthToTail(head, 6) is None


if __name__ == '__main__':
    unittest.main()
