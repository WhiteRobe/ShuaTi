"""
题目来源:
    牛客网
    @See https://www.nowcoder.com/practice/d77d11405cc7470d82554cb392585106
    题目序号 剑指offer 22
题目描述:
    输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
    假设压入栈的所有数字均不相等。
    例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
    但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
思路:
    @See https://www.nowcoder.com/questionTerminal/d77d11405cc7470d82554cb392585106?f=discussion
    > 借用一个辅助的栈，遍历压栈顺序，先将第一个放入栈中，这里是1，然后判断栈顶元素是不是出栈顺序的第一个元素，这里是4，很显然1≠4，
    > 所以我们继续压栈，直到相等以后开始出栈，出栈一个元素，则将出栈顺序向后移动一位，直到不相等，
    > 这样循环等压栈顺序遍历完成，如果辅助栈还不为空，说明弹出序列不是该栈的弹出顺序
样例输入:
    [1, 2, 3, 4, 5], [4, 5, 3, 2, 1]
    [1, 2, 3, 4, 5], [4, 3, 5, 1, 2]
样例输出:
    True
    False
"""
from structure.stack import ListStack as Stack


class Solution:
    def IsPopOrder(self, pushV, popV):
        s, i, j, total_size = Stack(), 0, 0, len(pushV)
        while s.size() < total_size and j < len(popV):
            if pushV[i] != popV[j]:  # 空栈或不相等就考虑入栈
                if s.top() == popV[j]:  # 栈顶为要出栈的元素
                    s.pop()
                    j += 1
                else:  # 否则把不相同的元素入栈
                    s.push(pushV[i])
                    i = min(total_size-1, i + 1)  # 小心越界
            else:
                i, j = min(total_size-1, i + 1), j + 1

        return s.size() == 0 or len(pushV) == len(popV) == 0  # 注意空栈的影响
