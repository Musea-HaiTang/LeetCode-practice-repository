from collections import Counter
class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        return False

    @staticmethod
    def isAnagram2(s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# 使用Counter的实现：时间复杂度O(n)，空间复杂度O(n)
# 使用sorted的实现：时间复杂度O(n log n)，空间复杂度O(n)
# 2025.10.12
# 复习一次。2025.10.12
