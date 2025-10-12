"""
896. 单调数列(简单)
如果数组是单调递增或单调递减的，那么它是 单调 的。
如果对于所有 i <= j，nums[i] <= nums[j]，那么数组 nums 是单调递增的。
如果对于所有 i <= j，nums[i] >= nums[j]，那么数组 nums 是单调递减的。
当给定的数组 nums 是单调数组时返回 true。
否则返回 false。
"""
class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums) <= 2:
            return True

        # 判断是否为递增序列
        def is_increasing():
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    return False
            return True

        # 判断是否为递减序列
        def is_decreasing():
            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1]:
                    return False
            return True

        return is_increasing() or is_decreasing()


    def isMonotonic2(self, nums: list[int]) -> bool:
        increasing = decreasing = True
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                decreasing = False
            if nums[i] < nums[i-1]:
                increasing = False
        return increasing or decreasing

# 方法一：分两个方法来分别判断
# 方法二：通过双标记来判断
# 2025.10.12
# 复习一次。2025.10.12