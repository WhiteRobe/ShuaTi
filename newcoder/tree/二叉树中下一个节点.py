"""
题目来源:
    牛客网
    @See https://www.nowcoder.com/practice/9023a0c988684a53960365b889ceaf5e
    剑指offer 题58
题目描述:
    给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
思路:
    前序(Pre-Order Traversal)：根左右
    中序(In-Order Traversal)：左根右
    后续(Post-Order Traversal)：左右根

    一个节点若有右子树，则下一个节点为其右子树"最左节点“。
    一个节点如果没有右子树，需要进行回溯：
        1. 若其为父节点的左节点，则下一个节点为父节点
        2. 若其为父节点的右节点，则下一个节点为：沿着父节点链条向上直到遇到是它父节点左节点的节点，其父节点为下一个节点。
            (递归途中，如果遇到的为右节点，继续向上)
样例输入:

样例输出:

"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None  # 指向父节点


class Solution:
    def GetNext(self, node):
        if node.right is not None:
            child = node.right
            while child.left is not None:
                child = child.left
            return child
        else:
            me, father = node, node.next
            while father is not None and (father.left is None or father.left.val != me.val):
                me = father
                father = father.next
            return father
