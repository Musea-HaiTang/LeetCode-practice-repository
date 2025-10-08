class Solution:
    def arraySign(self, nums: list[int]) -> int:
        nnum = 0
        for i in nums:
            if i < 0:
                nnum +=1
            else:
                return 0
        if nnum % 2 == 0:
            return 1
        else:
            return -1
