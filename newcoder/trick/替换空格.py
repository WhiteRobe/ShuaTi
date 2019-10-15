"""
题目来源：
    牛客网
    @See https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423
    剑指offer 题4
题目描述
    请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
思路:
    1. replace(' ', '%20')
    2. 一个空间复杂度为O(n)算法，且不占用额外空间，主要针对C语言进行优化：
        已知空格替换为'%20'，每替换一次原字符串长度+2。如果从头扫到位，发现一次空格，把空格之后的所有字符串都后移动两位然后写入'%20'效率太差
        更改思路：先扫一边字符串确定空格的数量，然后给定两个指针i和j，分别指向原串末尾和空格替换后的末尾，然后从后往前扫
            当遇到空格时，向后复制单词，然后在i处插入'%20'
样例输入:
    We Are Happy
样例输出：
    We%20Are%20Happy
"""


# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        # return s.replace(' ', '%20')  # 直接调API当然可以，但可以换个类似C语言的方式实现：
        s = list(s)  # python str对象必须转成list才可以像C中一样操作，这不算额外的空间
        count = 0
        for i in range(len(s)):
            if s[i] == ' ':
                count += 1
        i, j, s = len(s)-1, len(s) + 2 * count - 1, s + [''] * 2 * count

        for _ in range(i, -1, -1):
            if s[_] == ' ':
                s[j-2:j+1] = '%20'
                j -= 3
            else:
                s[j] = s[_]
                j -= 1
        return ''.join(s)  # 同样该行也是为了还原C语言的*char
        # 对于python还可以更方便的不借助API实现，而这个步骤还原到C语言里其实是占用了额外空间的
        # s = list(s)
        # for i in range(len(s)):
        #     if s[i] == ' ':
        #         s[i] = '%20'
        # return ''.join(s)


