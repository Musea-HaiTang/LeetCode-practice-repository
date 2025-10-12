"""
1822. 数组元素积的符号(简单)
已知函数 signFunc(x) 将会根据 x 的正负返回特定值。
如果 x 是正数，返回 1。
如果 x 是负数，返回 -1。
如果 x 是等于 0，返回 0。
给你一个整数数组 nums。
令 product 为数组 nums 中所有元素值的乘积。
返回 signFunc(product)。
"""
class Solution:
    @staticmethod
    def arraySign(nums: list[int]) -> int:
        n_num = 0
        for i in nums:
            if i < 0:
                n_num +=1
            elif i > 0:
                continue
            else:
                return 0
        if n_num % 2 == 0:
            return 1
        else:
            return -1


    @staticmethod
    def arraySign2(nums: list[int]) -> int:
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign = -sign
        return sign
