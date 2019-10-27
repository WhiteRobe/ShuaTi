"""
题目来源:
    LeetCode
    @See https://leetcode-cn.com/contest/weekly-contest-160/problems/find-positive-integer-solution-for-a-given-equation/
    题目序号 5238 周赛60
题目描述:
    给出一个函数  f(x, y) 和一个目标结果 z，请你计算方程 f(x,y) == z 所有可能的正整数 数对 x 和 y。

    给定函数是严格单调的，也就是说：

        f(x, y) < f(x + 1, y)
        f(x, y) < f(x, y + 1)
    函数接口定义如下：

        interface CustomFunction {
        public:
          // Returns positive integer f(x, y) for any given positive integer x and y.
          int f(int x, int y);
        };

    如果你想自定义测试，你可以输入整数 function_id 和一个目标结果 z 作为输入，
    其中 function_id 表示一个隐藏函数列表中的一个函数编号，题目只会告诉你列表中的 2 个函数。

    你可以将满足条件的 结果数对 按任意顺序返回。
思路:
    暴力解会超时，所以需要考虑单调性
样例输入:
    function_id = 1, z = 5
样例输出:
    [[1,4],[2,3],[3,2],[4,1]]  # function_id = 1 表示 f(x, y) = x + y
提示：

    1 <= function_id <= 9
    1 <= z <= 100
    题目保证 f(x, y) == z 的解处于 1 <= x, y <= 1000 的范围内。
    在 1 <= x, y <= 1000 的前提下，题目保证 f(x, y) 是一个 32 位有符号整数。
"""
from typing import List

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
"""


class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        return x + y


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        results = []
        i, j, over = 1, 1, False
        while i <= 1000 and not over:
            j = 1
            while j <= 1000 and not over:
                cal = customfunction.f(i, j)
                if cal == z:
                    results.append([i, j])
                elif cal > z:
                    over = (j == 1)
                    break
                j += 1
            i += 1
        return results