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
