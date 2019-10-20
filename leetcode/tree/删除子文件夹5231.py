"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/contest/weekly-contest-159/problems/remove-sub-folders-from-the-filesystem/
    题目序号 周赛159 5231
题目描述:
    你是一位系统管理员，手里有一份文件夹列表 folder，你的任务是要删除该列表中的所有 子文件夹，并以 任意顺序 返回剩下的文件夹。

    我们这样定义「子文件夹」：
        如果文件夹 folder[i] 位于另一个文件夹 folder[j] 下，那么 folder[i] 就是 folder[j] 的子文件夹。

    文件夹的「路径」是由一个或多个按以下格式串联形成的字符串：
        / 后跟一个或者多个小写英文字母。
        例如，/leetcode 和 /leetcode/problems 都是有效的路径，而空字符串和 / 不是。
思路:
    前缀树或者直接搜索子串
样例输入:
    folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    folder = ["/a","/a/b/c","/a/b/d"]
    folder = ["/a/b/c","/a/b/d","/a/b/ca"]
样例输出:
    ["/a","/c/d","/c/f"]
    ["/a"]
    ["/a/b/c","/a/b/ca","/a/b/d"]
提示：
    1 <= folder.length <= 4 * 10^4
    2 <= folder[i].length <= 100
    folder[i] 只包含小写字母和 /
    folder[i] 总是以字符 / 起始
    每个文件夹名都是唯一的
"""
from typing import List


class Solution:
    class FileTreeNode:
        def __init__(self, v):
            self.val = v
            self.child = {}

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root, results = Solution.FileTreeNode('/'), []
        folder.sort(key=lambda i: len(i), reverse=False)  # 长度短的在前
        for folder_path in folder:
            c, is_child = root, False
            for node in folder_path.split('/')[1:]:  # [1:]是因为 nodes[0] is ''
                if node not in c.child.keys():
                    c.child[node] = Solution.FileTreeNode(node)
                elif not c.child[node].child:  # 树已经到了根部
                    is_child = True
                    break
                c = c.child[node]
            if not is_child:
                results.append(folder_path)
        return results
