import unittest
from newcoder.linklist import 反转链表 as tT


def to_array(head):
    result = []
    while head:
        result += [head.val]
        head = head.next
    return result


def datasets():
    nodes = [MyTestCase.ListNode(i) for i in range(0, 6)]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    nodes[2].next = nodes[3]
    nodes[3].next = nodes[4]
    nodes[4].next = nodes[5]
    return nodes[0]


class MyTestCase(unittest.TestCase):
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def test_ins1(self):
        s = tT.Solution()
        head = s.ReverseList(datasets())
        self.assertEqual(to_array(head), [5, 4, 3, 2, 1, 0])

    def test_one_element(self):
        s = tT.Solution()
        head = s.ReverseList(MyTestCase.ListNode(0))
        self.assertEqual(to_array(head), [0])

    def test_empty(self):
        s = tT.Solution()
        head = s.ReverseList(None)
        self.assertEqual(to_array(head), [])


if __name__ == '__main__':
    unittest.main()
