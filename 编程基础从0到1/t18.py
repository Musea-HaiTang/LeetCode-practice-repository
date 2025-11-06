"""
1672. 最富有客户的资产总量(简单)
给你一个 m x n 的整数网格 accounts
其中 accounts[i][j] 是第 i 位客户在第 j 家银行托管的资产数量
返回最富有客户所拥有的资产总量
客户的资产总量就是他们在各家银行托管的资产数量之和
最富有客户就是资产总量最大的客户
"""


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for acc in accounts:
            total = sum(acc)
            if total > max_wealth:
                max_wealth = total
        return max_wealth



class Solution2:
    def maximumWealth2(self, accounts: list[list[int]]) -> int:
        return max(map(sum, accounts))

        # 稍微直接一点，比较容易看懂
        # return max([sum(acc) for acc in accounts])

# 学习代码真的是不进则退，我自己写出来的就很丑陋，而且还不对，真的一下不写就容易忘记
# 2025.11.6