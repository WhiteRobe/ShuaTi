"""
题目来源：
    牛客网
    @See https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3
    剑指offer 题9
题目描述
    大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第一项为1）。n<=39
思路:
    递归实现会多次求一个重复的值，延缓算法的速度。如 f(5) = f(4) + f(3) = (f(3) + f(2)) + f(3), f(3)被重复求取
    因此使用迭代实现，可以最好的实现算法
样例输入:
    
样例输出：
    
"""


class Solution:
    def fibonacci(self, n):
        # write code here
        if n <= 1:
            return n
        # return self.Fibonacci(n-2) + self.Fibonacci(n-1) 
        # 以上方法会超时，递归方式求解会重复求值
        dec_one, dec_two = 1, 0
        for i in range(n-2):
            dec_one, dec_two = dec_one + dec_two, dec_one
        return dec_one + dec_two

