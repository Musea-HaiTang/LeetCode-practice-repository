"""
459. 重复的子字符串(简单)

给定一个非空的字符串 s
检查是否可以通过由它的一个子串重复多次构成
"""
class Solution:
    @staticmethod
    def repeatedSubstringPattern(s: str) -> bool:
        # 方法一：枚举子串长度
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                if s[:i] * (n // i) == s:
                    return True
        return False

    # 或者更简洁的方法（推荐）
    @staticmethod
    def repeatedSubstringPattern_smart(s: str) -> bool:
        return s in (s + s)[1:-1]

# 有点难啊，家人们，这是简单题吗？
# 2025.10.6
# 复习一次。2025.10.12
