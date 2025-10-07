class Solution:
    @staticmethod
    def moveZeroes(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 使用双指针技术，原地移动非零元素到前面
        left = 0  # 指向下一个非零元素应该放置的位置

        # 第一遍遍历：将所有非零元素移到数组前部
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]  # 将非零元素移动到left位置
                left += 1

        # 第二遍遍历：将剩余位置填充为0
        while left < len(nums):
            nums[left] = 0
            left += 1



    @staticmethod
    def moveZeroes2(nums: list[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]   # 交换非零元素到左边去，一个一个填满
                left += 1
            right += 1

