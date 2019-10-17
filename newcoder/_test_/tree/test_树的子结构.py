import unittest
from newcoder.tree import 树的子结构 as tT
from structure.tree_node import TreeNode


def datasets():
    ns = [TreeNode(i) for i in [8, 8, 7, 9, 2, 4, 7]]
    ns[0].left, ns[0].right = ns[1], ns[2]
    ns[1].left, ns[1].right = ns[3], ns[4]
    ns[4].left, ns[4].right = ns[5], ns[6]
    return ns


class MyTestCase(unittest.TestCase):
    def test_empty(self):
        s = tT.Solution()
        root = datasets()[0]
        self.assertFalse(s.HasSubtree(root, None))
        self.assertFalse(s.HasSubtree(None, root))

    def test_normal(self):
        s = tT.Solution()
        root = datasets()[0]
        ns2 = datasets()
        ns2[4].left, ns2[4].right = None, None
        self.assertTrue(s.HasSubtree(root, ns2[0]))

    def test_normal_2(self):
        s = tT.Solution()
        root = datasets()[0]
        ns2 = datasets()
        ns2[4].val, ns2[4].left, ns2[4].right = 111, None, None
        self.assertFalse(s.HasSubtree(root, ns2[0]))


if __name__ == '__main__':
    unittest.main()
