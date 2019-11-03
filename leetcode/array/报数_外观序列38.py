"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/problems/count-and-say/
    题目序号 38
题目描述:
    报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
        1.     1
        2.     11
        3.     21
        4.     1211
        5.     111221
        6.     312211
        7.     13112221
    1 被读作  "one 1"  ("一个一") , 即 11。
    11 被读作 "two 1s" ("两个一"）, 即 21。
    21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
        下一个数是对上一个数的描述，
        比方说 1211 里有 “ 1 个 1 ， 1 个 2 ， 2 个 1 ” ，那么 111221 就是它的下一个数。
思路:
    递归即可
样例输入:
    4
样例输出:
    1211
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        last_str = self.countAndSay(n-1)
        num, char, res = 0, '', ""
        for i in last_str:
            if char != i:
                res += (str(num) + char) if num else ""
                num, char = 1, i
            else:
                num += 1
        return res + str(num) + char
