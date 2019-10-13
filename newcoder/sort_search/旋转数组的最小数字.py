"""
题目来源:
    牛客网
    @See https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba
题目描述:
    把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
    输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
    例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
    NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
思路:
    实际上是一个二分查找：
        给定前后两个索引head, tail，当出现 s[head] <= s[tail] 时，最小值为 s[head]，否则 head + 1 = tail时找到，最小值为tail

    当二分查找过程中，对于以下情况，就只能顺序查找了：
        2 3 0 2 2 2 2
        2 2 2 2 0 1 2
样例输入:

样例输出:

"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        head, tail, mid = 0, len(rotateArray)-1, 0
        if tail < 0:
            return 0

        while rotateArray[head] >= rotateArray[tail]:

            if tail - head == 1:
                mid = tail
                break

            mid = (head + tail) // 2

            if rotateArray[head] == rotateArray[mid] == rotateArray[tail]:
                return self.order_search(rotateArray[head: tail+1])

            if rotateArray[head] <= rotateArray[mid]:
                head = mid
            elif rotateArray[mid] <= rotateArray[tail]:
                tail = mid

        return rotateArray[mid]

    def order_search(self, array):
        # or just min(array)
        # 可以采用双指针进一步加速
        result = float('inf')
        for i in array:
            if result > i:
                result = i
        return result
