"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/contest/weekly-contest-160/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
    题目序号 5240 周赛16
题目描述:
    给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，
    **如果 s 中的每一个字符都只出现过一次**，那么它就是一个可行解。

    请返回所有可行解 s 中最长长度。
思路:
    值比较少，暴力即可
    可以考虑排个序，让长串的在前，有效减少时间开销
样例输入:
    arr = ["un","iq","ue"]
样例输出:
    4
    解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。
提示：
    1 <= arr.length <= 16
    1 <= arr[i].length <= 26
    arr[i] 中只含有小写英文字母
"""
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = list(filter(lambda x: len(x) == len(set([_ for _ in x])), arr))  # 过滤重复元素

        # 简单排个序
        hmap = self.get_map(arr)
        hmap = self.get_map(sorted(hmap, key=lambda x: hmap[x], reverse=True))

        sorted_arr = list(hmap.keys())
        max_len = hmap[sorted_arr[0]] if len(sorted_arr) > 0 else 0

        for i in range(len(hmap)):
            s1 = set([_ for _ in sorted_arr[i]])
            for j in range(i+1, len(hmap)):
                s2 = set([_ for _ in sorted_arr[j]])
                if not s1 & s2:  # 如果是空集则延长字串
                    s1 = s1 | s2
                    max_len = max(max_len, len(s1))

        return max_len

    def get_map(self, arr: List[str]):
        arr_lens, hmap = list(map(lambda x: len(x), arr)), {}
        for s, l in zip(arr, arr_lens):
            hmap[s] = l
        return hmap