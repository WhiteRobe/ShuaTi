import unittest
from newcoder.linklist import 从尾到头打印链表 as tT


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TestFunc(unittest.TestCase):
    def test_replaceSpace(self):
        head = ListNode(1)
        c = head
        c.next = ListNode(2)
        c = c.next
        c.next = ListNode(3)
        c = None

        assert tT.Solution().printListFromTailToHead(head) == [3, 2, 1]
        assert tT.Solution().printListFromTailToHead(None) == []


if __name__ == '__main__':
    unittest.main()
