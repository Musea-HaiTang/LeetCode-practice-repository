"""
14. 最长公共前缀(简单)

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。


示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
"""

class Solution:
    @staticmethod
    def longest_common_prefix(strs: list[str]) -> str:
        s0 = strs[0]
        for j ,c in enumerate(s0):
            for i in strs:
                if j == len(i) or c != i[j]:
                    return s0[:j]
        return s0

    # enumerate函数可以将一个序列中的元素和索引进行同时处理，
    # 如enumerate("abc")，返回(0, 'a'), (1, 'b'), (2, 'c')

    #这道题无思路，需要复习2025.10.1
