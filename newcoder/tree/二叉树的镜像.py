"""
题目来源:
    牛客网
    @See https://www.nowcoder.com/practice/564f4c26aa584921bc75623e48ca3011
    题目序号 19
题目描述:
    操作给定的二叉树，将其变换为源二叉树的镜像
思路:
    先序遍历每个点，若有子节点则交换左右节点
样例输入:
    二叉树的镜像定义：源二叉树 
            8
           /  \
          6   10
         / \  / \
        5  7 9 11
样例输出:
        镜像二叉树
            8
           /  \
          10   6
         / \  / \
        11 9 7  5
"""
from structure.tree_node import TreeNode


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root:
            root.left, root.right = root.right, root.left
            self.Mirror(root.left)
            self.Mirror(root.right)
        return root


