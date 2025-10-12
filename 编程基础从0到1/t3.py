"""
28. 找出字符串中第一个匹配项的下标(简单)
给你两个字符串 haystack 和 needle。
请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
如果 needle 不是 haystack 的一部分，则返回 -1。
"""

class Solution:
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


    # 使用python内置的find方法,和上面的方法一模一样
    @staticmethod
    def strStr2(haystack: str, needle: str) -> int:
        return haystack.find(needle)

# 匹配字符串，这个还是很实用的
# 还有更高效的方法：KMP算法
# 2025.10.4