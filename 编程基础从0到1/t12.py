"""
58. 最后一个单词的长度(简单)
给你一个字符串 s，由若干个单词组成，单词前后用一些空格字符隔开。
返回字符串中 最后一个 单词的长度。
单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split( )
        return len(s_list[-1])
# very easy
# 只花了半分钟，就写出来了
# 2025.10.14