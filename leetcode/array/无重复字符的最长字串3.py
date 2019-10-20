"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
    题目序号 3
题目描述:
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
思路:
    定义字符到索引的映射，而不是使用迭代来判断一个字符是否存在
    map = { char: char_at_index }
    如果判断存在，则更新无重复序列的的左端点 i
样例输入:
    abcabcbb
    bbbbb
    pwwkew
    qw
样例输出:
    3
    1
    3
    2
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap, max_len, i = {}, 0, -1  # i从-1开始
        for j, c in enumerate(s):
            if c in hmap:  # 调整i的位置
                i = max(hmap.get(c), i)
            max_len = max(max_len, j - i)
            hmap.update({c: j})  # 新无重复c字符的索引

        return max_len
