"""
题目来源：
    牛客网
    @See https://www.nowcoder.com/practice/beb5aa231adc45b2a5dcc5b62c93f593?tpId=13&tqId=11166&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
题目描述
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分
    并保证奇数和奇数，偶数和偶数之间的相对位置不变。
思路:
    1. 扫描，划分为两个数组；叠加数组输出。Python牛逼
    2. 给定两个链表头，分别指向奇数和偶数的链表。大致同上，下略。
    3. 类似冒泡
样例输入:
    [1,2,3,4,5,6,7]
    [2,4,6,1,3,5,7]
样例输出：
    [1,3,5,7,2,4,6]
    [1,3,5,7,2,4,6]
"""


class Solution:
    def baseline(self, a):
        # 兼容扩展，如 %3 等
        return a & 0b1

    def reOrderArray(self, array):
        # write code here
        odd, even, length = [], [], len(array)
        for i in range(length):
            # 等价于：odd.append(array[i]) if array[i] & 0b1 == 1 else even.append(array[i])
            res = odd if self.baseline(array[i]) else even
            res.append(array[i])
        return odd + even


# if __name__ == '__main__':
#     s = Solution()
#     assert s.reOrderArray([1, 2, 3, 4, 5, 6, 7]) == [1, 3, 5, 7, 2, 4, 6]
#     assert s.reOrderArray([2, 4, 6, 1, 3, 5, 7]) == [1, 3, 5, 7, 2, 4, 6]
