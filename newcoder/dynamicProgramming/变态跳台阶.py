# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        assert number > 0
        a = 1
        return a << (number-1)  # 位运算解决一切 等效于 pow(2, number-1)

# 牛客网
# @See https://www.nowcoder.com/practice/22243d016f6b47f2a6928b4313c85387?tpId=13&tqId=11162&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
# 思路: f(n)=f(n-1)+f(n-2)+f(n-3)... | 代入f(n-1)=f(n-2)+f(n-3)... |可得 f(n)=2*f(n-1)
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。


# if __name__ == '__main__':
#     s = Solution()
#     assert s.jumpFloorII(1) == 1
#     assert s.jumpFloorII(2) == 2
#     assert s.jumpFloorII(3) == 4
#     assert s.jumpFloorII(4) == 8
#     assert s.jumpFloorII(5) == 16
