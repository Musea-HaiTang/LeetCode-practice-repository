"""
1572. 矩阵对角线元素的和(简单)
给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。
请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。
示例  1：
输入：mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
输出：25
解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
请注意，元素 mat[1][1] = 5 只会被计算一次。
"""
class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        return sum(mat[i][j] for i in range(n) for j in range(n) \
                    if i == j or i + j == n - 1)

    def diagonalSum2(self, mat: list[list[int]]) -> int:
        n = len(mat)
        total = 0
        mid = n // 2
        for i in range(n):
            total += mat[i][i] + mat[i][n - 1 - i]
        return total - mat[mid][mid] * (n & 1)

# 我发现自己对于列表的推导式还是用的不熟练，不会用，得多多熟悉
# 2025.11.7








