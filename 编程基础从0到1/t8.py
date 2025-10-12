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
