"""
1. 两数之和
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。
示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
"""

class Solution:
    @staticmethod
    def two_sum(numbers: list[int], target_sum: int) -> list[int] | None:
        length =len(numbers)
        for i in range(length):
            for j in range(i+1,length):
                if numbers[i]+numbers[j] == target_sum:
                    return [i,j]
        return None


while True:
    try:
        # 将输入的字符串转换为整数列表
        nums = list(map(int, input("Enter the list of numbers (space-separated): ").split()))

        # 将目标值字符串转换为整数
        target = int(input("Enter the target: "))

        result = Solution.two_sum(nums, target)
        print(result)
        break
    except ValueError:
        print("输入格式错误，请确保输入的都是数字")
    except Exception as e:
        print(f"发生错误: {e}")

