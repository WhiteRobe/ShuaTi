import unittest
from newcoder.tree import 重建二叉树 as tT


TreeNode = tT.TreeNode


def check(answer, root):
    if root is None and answer is None:
        return
    assert answer.val == root.val
    check(answer.left, root.left)
    check(answer.right, root.right)


def datasets():
    pot = [1, 2, 4, 7, 3, 5, 6, 8]
    iot = [4, 7, 2, 1, 5, 3, 8, 6]
    tree_nodes = [TreeNode(i) for i in range(0, 9)]
    tree_nodes[1].left = tree_nodes[2]
    tree_nodes[1].right = tree_nodes[3]
    tree_nodes[2].left = tree_nodes[4]
    tree_nodes[4].right = tree_nodes[7]
    tree_nodes[3].left = tree_nodes[5]
    tree_nodes[3].right = tree_nodes[6]
    tree_nodes[6].left = tree_nodes[8]
    return pot, iot, tree_nodes[1]


class MyTestCase(unittest.TestCase):
    def test_reConstructBinaryTree(self):
        s = tT.Solution()
        pot, iot, answer = datasets()
        check(answer, s.reConstructBinaryTree(pot, iot))


if __name__ == '__main__':
    unittest.main()
