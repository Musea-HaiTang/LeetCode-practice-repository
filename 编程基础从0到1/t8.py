"""
1502. 判断能否形成等差数列(简单)
给你一个数字数组 arr。
如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列。
如果可以重新排列数组形成等差数列，请返回 true。
否则，返回 false。
"""

class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        if len(arr) < 2:
            return True
        # 冒泡排序
        # for i in range(len(arr)):
        #     for j in range(len(arr)-1-i):
        #         if arr[j] > arr[j+1]:
        #             arr[j], arr[j+1] = arr[j+1], arr[j]

        arr.sort()# 排序

        for x in range(1,len(arr) - 1):
            if arr[x] * 2 != arr[x+1] + arr[x+1]:
                return False
        return True
# 排序算法，数组.sort()
# 冒泡排序，时间复杂度 O(n^2)
# 2025.10.12