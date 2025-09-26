class Solution:
    @staticmethod
    def two_sum(numbers: list[int], target_sum: int) -> list[int] | None:
        length =len(numbers)
        for i in range(length):
            for j in range(i+1,length):
                if numbers[i]+numbers[j] == target_sum:
                    return [i,j]
        return None

try:
    # 将输入的字符串转换为整数列表
    nums = list(map(int, input("Enter the list of numbers (space-separated): ").split()))

    # 将目标值字符串转换为整数
    target = int(input("Enter the target: "))

    result = Solution.two_sum(nums, target)
    print(result)
except ValueError:
    print("输入格式错误，请确保输入的都是数字")
except Exception as e:
    print(f"发生错误: {e}")

