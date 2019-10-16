import unittest
from newcoder.linklist import 合并两个排序的链表 as tT


def datasets(end=10):
    nodes1 = [MyTestCase.ListNode(i) for i in range(0, end, 2)]
    for i in range(len(nodes1)-1):
        nodes1[i].next = nodes1[i + 1]
    nodes2 = [MyTestCase.ListNode(i) for i in range(1, end, 2)]
    for i in range(len(nodes2)-1):
        nodes2[i].next = nodes2[i + 1]
    return nodes1[0], nodes2[0]


def to_array(head):
    result = []
    while head:
        result += [head.val]
        head = head.next
    return result


class MyTestCase(unittest.TestCase):
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def test_one_empty(self):
        n1, n2 = datasets()
        s = tT.Solution()
        self.assertEqual([0, 2, 4, 6, 8], to_array(s.Merge(n1, None)))
        self.assertEqual([1, 3, 5, 7, 9], to_array(s.Merge(None, n2)))

    def test_two_empty(self):
        s = tT.Solution()
        self.assertEqual([], to_array(s.Merge(None, None)))

    def test_normal(self):
        s = tT.Solution()
        n1, n2 = datasets()
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], to_array(s.Merge(n1, n2)))

    def test_normal_with_equal_value(self):
        s = tT.Solution()
        n1, n2 = datasets()
        n2.val = n1.val
        n1.next.val = n2.next.val
        self.assertEqual([0, 0, 3, 3, 4, 5, 6, 7, 8, 9], to_array(s.Merge(n1, n2)))

    def test_not_equal_len(self):
        s = tT.Solution()
        n1, n2 = datasets()
        n2.next.next.next = None
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 8], to_array(s.Merge(n1, n2)))


if __name__ == '__main__':
    unittest.main()
