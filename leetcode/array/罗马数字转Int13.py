"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/problems/roman-to-integer/
    题目序号 13
题目描述:
    罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

        字符          数值
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
    例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

    通常情况下，罗马数字中小的数字在大的数字的右边。
    但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
    同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

        I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
        X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
        C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
        给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
思路:
    - 一次读两位并且判定即可
    - 用哈希表
样例输入:
    "III"
    "IV"
    "IX"
    "LVIII"
    "MCMXCIV"
样例输出:
    3
    4
    9
    58
    1994
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        func = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        res, i, total_len = 0, 0, len(s)
        while i < total_len:
            ro = s[i:i+2] if i != total_len-1 else s[i]
            if ro not in func.keys():
                ro = s[i]
            res += func[ro]
            i += len(ro)
        return res
