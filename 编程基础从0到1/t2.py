from collections import Counter

class Solution:
    # 方法一，比较基础
    @staticmethod
    def findTheDifference(s: str, t: str) -> str:
        # 使用字符计数的方法
        char_count = {}

        # 统计s中每个字符的出现次数
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # 遍历t中的字符
        for char in t:
            # 如果字符不在s中或者已经用完计数
            if char not in char_count or char_count[char] == 0:
                return char
            # 减少该字符的计数
            char_count[char] -= 1

        # 理论上不会到达这里，但为了语法正确性
        return ""

    # 方法二，最好的方法
    @staticmethod
    def findTheDifference2(s: str, t: str) -> str:
        return list(Counter(t) - Counter(s))[0]

    # 方法三，这个逻辑相对清晰，但是没有方法二好
    @staticmethod
    def findTheDifference3(s: str, t: str) -> str:
        for char in t:
            if t.count(char) > s.count(char):
                return char
        return  ""
# 复习一次。2025.10.12
