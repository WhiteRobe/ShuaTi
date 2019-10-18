import unittest
from structure.tree_node import TreeNode
from newcoder.tree import 二叉树的镜像 as tT


def datasets():
    ns = [TreeNode(i) for i in [8, 6, 10, 5, 7, 9, 11]]
    ns[0].left, ns[0].right = ns[1], ns[2]
    ns[1].left, ns[1].right = ns[3], ns[4]
    ns[4].left, ns[4].right = ns[5], ns[6]

    ns_r = [TreeNode(i) for i in [8, 6, 10, 5, 7, 9, 11]]
    ns_r[0].right, ns_r[0].left = ns_r[1], ns_r[2]
    ns_r[1].right, ns_r[1].left = ns_r[3], ns_r[4]
    ns_r[4].right, ns_r[4].left = ns_r[5], ns_r[6]
    return ns, ns_r


def datasets_complete():
    ns = [TreeNode(i) for i in [8, 6, 10, 5, 7, 9, 11]]
    ns[0].left, ns[0].right = ns[1], ns[2]
    ns[1].left, ns[1].right = ns[3], ns[4]
    ns[2].left, ns[2].right = ns[5], ns[6]

    ns_r = [TreeNode(i) for i in [8, 6, 10, 5, 7, 9, 11]]
    ns_r[0].right, ns_r[0].left = ns_r[1], ns_r[2]
    ns_r[1].right, ns_r[1].left = ns_r[3], ns_r[4]
    ns_r[2].right, ns_r[2].left = ns_r[5], ns_r[6]
    return ns, ns_r


def to_array(res, node=None):
    if node is None:
        return res
    res.append(node.val)
    res = to_array(res, node.left)
    res = to_array(res, node.right)
    return res


class MyTestCase(unittest.TestCase):
    def test_complete_tree(self):
        s = tT.Solution()
        ns_l, ns_r = datasets_complete()
        self.assertEqual(to_array([], s.Mirror(ns_l[0])), to_array([], ns_r[0]))

    def test_normal_tree(self):
        s = tT.Solution()
        ns_l, ns_r = datasets()
        self.assertEqual(to_array([], s.Mirror(ns_l[0])), to_array([], ns_r[0]))


if __name__ == '__main__':
    unittest.main()
