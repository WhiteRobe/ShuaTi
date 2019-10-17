"""
题目来源:
    牛客网
    @See https://www.nowcoder.com/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6
    @wiki https://zh.wikipedia.org/wiki/%E6%A0%91%E7%9A%84%E9%81%8D%E5%8E%86
    剑指offer 题6
题目描述:
    输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
    假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
    例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
思路:
    前序(Pre-Order Traversal)：根左右
    中序(In-Order Traversal)：左根右
    后续(Post-Order Traversal)：左右根

    先从先序中找到根节点，在在中序中该根节点左侧为左子树，右侧为右子树；循环这个过程构建整棵树
样例输入:
    {1, 2, 4, 7, 3, 5, 6, 8}
    {4, 7, 2, 1, 5, 3, 8, 6}
样例输出:
           1
        2     3
     4      5   6
   7   8
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def divide_nodes(self, pot, iot):
        if len(pot) == 0:
            return None, {'pot': [], 'iot': []}, {'pot': [], 'iot': []}
        root = TreeNode(pot[0])
        root_index_pot = pot.index(root.val)
        root_index_iot = iot.index(root.val)
        iot_left = iot[:root_index_iot]
        iot_right = iot[root_index_iot + 1:]
        pot_left = pot[root_index_pot + 1: root_index_pot + 1 + len(iot_left)]
        pot_right = pot[root_index_pot + len(iot_left) + 1:]
        return root, {'pot': pot_left, 'iot': iot_left}, {'pot': pot_right, 'iot': iot_right}

    def build(self, pot, iot):
        root, left, right = self.divide_nodes(pot, iot)
        if root is None:
            return None
        root.left = self.build(left['pot'], left['iot'])
        root.right = self.build(right['pot'], right['iot'])
        return root

    # 辅助函数
    def reConstructBinaryTree(self, pre, tin):
        return self.build(pre, tin)

    """
    def view(self, root):
        # 先序遍历
        if root is None:
            return
        print(root.val)
        self.view(root.left)
        self.view(root.right)
    """


# if __name__ == '__main__':
#     pot = [1, 2, 4, 7, 3, 5, 6, 8]
#     iot = [4, 7, 2, 1, 5, 3, 8, 6]
#     s = Solution()
#     print(s.build(pot, iot))
#     s.view(s.build(pot, iot))
