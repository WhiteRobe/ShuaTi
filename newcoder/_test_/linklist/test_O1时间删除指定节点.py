import unittest
from newcoder.linklist import O1时间删除指定节点 as tT


def datasets(end=7):
    nodes = [TestCase.ListNode(i) for i in range(0, end)]
    for i in range(end-1):
        nodes[i].next = nodes[i+1]
    return nodes[0], nodes


def to_array(head):
    result = []
    while head:
        result += [head.val]
        head = head.next
    return result


class TestCase(unittest.TestCase):
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def test_delete_head(self):
        head, nodes = datasets()
        s = tT.Solution()
        self.assertEqual(to_array(s.delete(head, nodes[0])), [1, 2, 3, 4, 5, 6])

    def test_delete_mid(self):
        head, nodes = datasets()
        s = tT.Solution()
        self.assertEqual(to_array(s.delete(head, nodes[3])), [0, 1, 2, 4, 5, 6])

    def test_delete_tail(self):
        head, nodes = datasets()
        s = tT.Solution()
        self.assertEqual(to_array(s.delete(head, nodes[6])), [0, 1, 2, 3, 4, 5])

    def test_delete_only_one(self):
        node = TestCase.ListNode(0)
        s = tT.Solution()
        self.assertEqual(to_array(s.delete(node, node)), [])

    def test_delete_not_in_linklist(self):
        head, nodes = datasets()
        head_2, nodes_2 = datasets(end=20)
        node_single = TestCase.ListNode(9)
        s = tT.Solution()
        self.assertEqual(to_array(s.delete(head, nodes_2[10])), [0, 1, 2, 3, 4, 5, 6])
        self.assertEqual(to_array(s.delete(head, node_single)), [0, 1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
