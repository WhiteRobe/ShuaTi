"""
题目来源:
    牛客网
    @See https://www.nowcoder.com/practice/6a296eb82cf844ca8539b57c23e6e9bf
    题目序号 剑指offer 30
题目描述:
    输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
    如果找不到K个数应该返回一个空列表
思路:
    最大堆
    保持堆顶为最大的数
样例输入:
    [1, 2, 3, 4, 2] 3
    [1, 2, 3, 4] 8
样例输出:
    [1, 2, 2]
    []
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        import heapq
        return heapq.nsmallest(k, tinput) if len(tinput) >= k else []
