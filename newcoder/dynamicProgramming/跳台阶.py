# -*- coding:utf-8 -*-
class Solution:

    def jumpFloor(self, number):
        # write code here
        assert number >= 1
        jump_one, jump_two = 1, 2
        if number == 1:
            return jump_one
        elif number == 2:
            return jump_two
        else:
            for i in range(3, number+1):
                jump_one, jump_two = jump_two, jump_one + jump_two
        return jump_two


# 牛客网
# @See https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4
# 思路 @See https://blog.csdn.net/Shenpibaipao/article/details/88373195#22__93
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。


# if __name__ == '__main__':
#     s = Solution()
#     assert s.jumpFloor(1) == 1
#     assert s.jumpFloor(2) == 2
#     assert s.jumpFloor(3) == 3
#     assert s.jumpFloor(4) == 5
#     assert s.jumpFloor(5) == 8
