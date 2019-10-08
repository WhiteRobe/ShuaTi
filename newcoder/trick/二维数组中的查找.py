"""
题目来源：
    牛客网
    @See https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
题目描述
    在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
    请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
思路:
    数组有序，从左下开始扫描，若目标大于左侧第一个数，向右查询，否则直接上移一行。
样例输入:
    6
    1 2 3
    5 6 10
    7 9 11
    8 10 12
    6
    1 5 7 8
    2 6 9 10
    3 10 11 12
样例输出：
    True
"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows, cols = len(array), len(array[0])
        if rows == 1:
            return False
        for i in range(rows-1, -1, -1):
            if target < array[i][0]:
                continue
            for j in range(cols):
                if target == array[i][j]:
                    return True
                elif target < array[i][j]:
                    break
        return False


# if __name__ == '__main__':
#     s = Solution()
#     assert s.Find(6, [[1, 2, 3], [5, 6, 10], [7, 9, 11], [8, 10, 12]]) is True
#     assert s.Find(6, [[1, 5, 7, 8], [2, 6, 9, 10], [3, 10, 11, 12]]) is True
#     assert s.Find(7, [[]]) is False

