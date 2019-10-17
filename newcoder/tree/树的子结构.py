"""
题目来源:
    牛客网
    @See https://www.nowcoder.com/practice/6e196c44c7004d15b1610b9afca8bd88
    题目序号 剑指Offer 18
题目描述:
    输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
思路:
    先找相同的根节点，然后递归遍历
样例输入:

样例输出:

"""


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # pRoot1 是树A
        is_contain = False
        if pRoot1 and pRoot2:  # 空B树直接返回false
            if pRoot1.val == pRoot2.val:  # 根节点相同
                is_contain = self.compare_two_tree(pRoot1, pRoot2)
            if not is_contain:
                is_contain = self.HasSubtree(pRoot1.left, pRoot2)
            if not is_contain:
                is_contain = self.HasSubtree(pRoot1.right, pRoot2)

        return is_contain

    def compare_two_tree(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True

        if pRoot1 is None:
            return False

        if pRoot1.val != pRoot2.val:
            return False

        return self.compare_two_tree(pRoot1.left, pRoot2.left) and self.compare_two_tree(pRoot1.right, pRoot2.right)

