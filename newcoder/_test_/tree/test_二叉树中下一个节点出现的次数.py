import unittest
from newcoder.tree import 二叉树中下一个节点出现的次数 as tT


TreeLinkNode = tT.TreeLinkNode


def datasets_1():
    treenodes = [TreeLinkNode(i) for i in range(0, 10)]
    treenodes[1].left = treenodes[2]
    treenodes[1].right = treenodes[3]
    treenodes[2].next = treenodes[1]
    treenodes[3].next = treenodes[1]

    treenodes[2].left = treenodes[4]
    treenodes[2].right = treenodes[5]
    treenodes[4].next = treenodes[2]
    treenodes[5].next = treenodes[2]

    treenodes[3].left = treenodes[6]
    treenodes[3].right = treenodes[7]
    treenodes[6].next = treenodes[3]
    treenodes[7].next = treenodes[3]

    treenodes[5].left = treenodes[8]
    treenodes[5].right = treenodes[9]
    treenodes[8].next = treenodes[5]
    treenodes[9].next = treenodes[5]
    return treenodes


def datasets_2():
    treenodes = [TreeLinkNode(i) for i in range(0, 4)]

    treenodes[1].left = treenodes[2]
    treenodes[2].left = treenodes[3]
    treenodes[3].next = treenodes[2]
    treenodes[2].next = treenodes[1]
    return treenodes


def datasets_3():
    treenodes = [TreeLinkNode(i) for i in range(0, 4)]

    treenodes[1].right = treenodes[2]
    treenodes[2].right = treenodes[3]
    treenodes[3].next = treenodes[2]
    treenodes[2].next = treenodes[1]
    return treenodes


class MyTestCase(unittest.TestCase):
    def test_GetNext_1(self):
        s = tT.Solution()
        ds = datasets_1()
        self.assertEqual(s.GetNext(ds[4]).val, ds[2].val)
        self.assertEqual(s.GetNext(ds[2]).val, ds[8].val)
        self.assertEqual(s.GetNext(ds[8]).val, ds[5].val)
        self.assertEqual(s.GetNext(ds[5]).val, ds[9].val)
        self.assertEqual(s.GetNext(ds[9]).val, ds[1].val)
        self.assertEqual(s.GetNext(ds[1]).val, ds[6].val)
        self.assertEqual(s.GetNext(ds[6]).val, ds[3].val)
        self.assertEqual(s.GetNext(ds[3]).val, ds[7].val)
        self.assertEqual(s.GetNext(ds[7]), None)

    def test_GetNext_2(self):
        s = tT.Solution()
        ds = datasets_2()
        self.assertEqual(s.GetNext(ds[1]), None)
        self.assertEqual(s.GetNext(ds[2]).val, ds[1].val)
        self.assertEqual(s.GetNext(ds[3]).val, ds[2].val)

    def test_GetNext_3(self):
        s = tT.Solution()
        ds = datasets_3()
        self.assertEqual(s.GetNext(ds[1]).val, ds[2].val)
        self.assertEqual(s.GetNext(ds[2]).val, ds[3].val)
        self.assertEqual(s.GetNext(ds[3]), None)


if __name__ == '__main__':
    unittest.main()
