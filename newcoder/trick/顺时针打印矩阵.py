"""
题目来源:
    牛客网
    @See https://www.nowcoder.com/practice/9b4c81a02cd34f76be2659fa0d54342a
    题目序号 剑指Offer 20
题目描述:
    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
思路:
    把矩阵想象成若干个圈，每次打印一个圈
样例输入:
    1 2 3 4
    5 6 7 8
    9 10 11 12
    13 14 15 16
样例输出:
    1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10
"""


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix, should_print=True):
        # write code here
        rows, cols = len(matrix), len(matrix[0])
        top, right, bottom, left = -1, cols, rows, -1  # 给定界限
        results, c, c_d = [], [0, 0], 0  # 结果集 当前坐标 当前方向
        # directions = [0, 1, 2, 3]  # 右 下 左 上

        while len(results) < rows * cols:
            delta_x = 1 if c_d == 1 else (-1 if c_d == 3 else 0)
            delta_y = 1 if c_d == 0 else (-1 if c_d == 2 else 0)

            fr, to = self.select_from_to(c_d, (top, right, bottom, left))

            for _ in range(fr+delta_x+delta_y, to, delta_x+delta_y):
                # index = 1 if abs(delta_x) else 0
                c[0 if abs(delta_x) else 1] = _  # 上下移动时
                results.append(matrix[c[0]][c[1]])

            c_d, top, right, bottom, left = self.shrink(c_d, (top, right, bottom, left))

        if should_print:
            self.out_print(results)

        return results

    def select_from_to(self, direction, boundary):
        """
        选择正确的遍历方向
        """
        top, right, bottom, left = boundary
        if direction == 0:
            return left, right
        elif direction == 1:
            return top, bottom
        elif direction == 2:
            return right, left
        elif direction == 3:
            return bottom, top

    def shrink(self, direction, boundary):
        """
        尺度放缩
        """
        top, right, bottom, left = boundary
        if direction == 0:
            top += 1
        elif direction == 1:
            right -= 1
        elif direction == 2:
            bottom -= 1
        elif direction == 3:
            left += 1

        return (direction + 1) % 4, top, right, bottom, left

    def out_print(self, arr):
        for i in arr:
            print(i)
