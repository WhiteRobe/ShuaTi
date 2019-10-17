import unittest
from leetcode.linklist import 两数相加2 as tT


def decode(l1):
    result = []
    while l1:
        result.append(l1.val)
        l1 = l1.next
    return result


class MyTestCase(unittest.TestCase):
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def test_equal_len(self):
        s = tT.Solution()
        l1, l2 = MyTestCase.ListNode(2), MyTestCase.ListNode(5)
        l1_2, l2_2 = MyTestCase.ListNode(4), MyTestCase.ListNode(6)
        l1_3, l2_3 = MyTestCase.ListNode(3), MyTestCase.ListNode(4)
        l1.next, l2.next = l1_2, l2_2
        l1_2.next, l2_2.next = l1_3, l2_3
        self.assertEqual([7, 0, 8], decode(s.addTwoNumbers(l1, l2)))

    def test_not_equal_len(self):
        s = tT.Solution()
        l1, l2 = MyTestCase.ListNode(7), MyTestCase.ListNode(5)
        l1_2, l2_2 = MyTestCase.ListNode(4), MyTestCase.ListNode(6)
        l1_3= MyTestCase.ListNode(3)
        l1.next, l2.next = l1_2, l2_2
        l1_2.next = l1_3
        self.assertEqual([2, 1, 4], decode(s.addTwoNumbers(l1, l2)))

    def test_add_zero(self):
        s = tT.Solution()
        l1, l2 = MyTestCase.ListNode(7), MyTestCase.ListNode(0)
        l1_2 = MyTestCase.ListNode(4)
        l1_3 = MyTestCase.ListNode(3)
        l1.next = l1_2
        l1_2.next = l1_3
        self.assertEqual([7, 4, 3], decode(s.addTwoNumbers(l1, l2)))
        self.assertEqual([7, 4, 3], decode(s.addTwoNumbers(l2, l1)))

    def test_add_remain_carry(self):
        s = tT.Solution()
        l1, l2 = MyTestCase.ListNode(5), MyTestCase.ListNode(8)
        self.assertEqual([3, 1], decode(s.addTwoNumbers(l1, l2)))
        self.assertEqual([3, 1], decode(s.addTwoNumbers(l2, l1)))


if __name__ == '__main__':
    unittest.main()
