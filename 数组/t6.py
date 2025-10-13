class Solution:
    # 我自己写的
    @staticmethod
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        i = n - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i -=1
            else:
                digits[i] +=1
                return digits
        if i < 0:
            digits.insert(0, 1)
        return digits


    #标准解法
    @staticmethod
    def plus_one(self, digits: list[int]) -> list[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i + 1, n):
                    digits[j] = 0
                return digits

        # digits 中所有的元素均为 9
        return [1] + [0] * n

# 发现了问题，我忘记了数组的逆序遍历，需要先补足一下知识点。
# 2025.10.2
# 2025.10.13，复习一次
