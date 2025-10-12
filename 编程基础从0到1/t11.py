"""
66. 加一(简单)
给定一个表示 大整数 的整数数组 digits，其中 digits[i] 是整数的第 i 位数字。
这些数字按从左到右，从最高位到最低位排列。
这个大整数不包含任何前导 0。
将大整数加 1，并返回结果的数字数组。
"""
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1  # 进位
                return digits
            digits[i] = 0  # 进位数字的右边数字都变成 0

        # digits 全是 9，加一后变成 100...00
        return [1] + digits

# for i in range(len(digits) - 1, -1, -1):
# 从最后一个开始，一直到第一个，以逆序遍历
# 因为range是包前不包后，所以-1到达不了，只能到0
# 2025.10.12

