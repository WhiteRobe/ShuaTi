"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/contest/weekly-contest-159/problems/check-if-it-is-a-straight-line/
    题目序号 周赛159 5230
题目描述:
    在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。
思路:
    计算斜率即可，需要注意水平/垂直线和单点/双点输入
样例输入:
    coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    coordinates = [[0,0]]
    coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
样例输出:
    true
    true
    false
提示：
    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates 中不含重复的点
"""
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        d = self.cal_grad(coordinates[0], coordinates[1])
        for i in range(2, len(coordinates) - 1):
            new_d = self.cal_grad(coordinates[i], coordinates[i+1])
            if new_d != d:
                return False
        return True

    def cal_grad(self, p1, p2):
        if p1[0] == p2[0]:
            return 'vertical'
        elif p1[1] == p2[1]:
            return 'horizontal'
        else:
            return (p2[1] - p1[1]) / (p2[0] - p1[0])
