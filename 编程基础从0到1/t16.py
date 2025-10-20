"""
1275. 找出井字棋的获胜者(简单)

井字棋 是由两个玩家 A 和 B 在 3 x 3 的棋盘上进行的游戏。
井字棋游戏的规则如下：
玩家轮流将棋子放在空方格 (' ') 上。
第一个玩家 A 总是用 'X' 作为棋子，而第二个玩家 B 总是用 'O' 作为棋子。
'X' 和 'O' 只能放在空方格中，而不能放在已经被占用的方格上。
只要有 3 个相同的（非空）棋子排成一条直线（行、列、对角线）时，游戏结束。
如果所有方块都放满棋子（不为空），游戏也会结束。
游戏结束后，棋子无法再进行任何移动。
给你一个数组 moves，其中 moves[i] = [rowi, coli] 表示第 i 次移动在 grid[rowi][coli]。
如果游戏存在获胜者（A 或 B），就返回该游戏的获胜者。
如果游戏以平局结束，则返回 "Draw"。
如果仍会有行动（游戏未结束），则返回 "Pending"。
你可以假设 moves 都 有效（遵循 井字棋 规则），网格最初是空的，A 将先行动。
"""


class Solution:
    """
    解决井字棋游戏结果判断问题

    该函数根据给定的移动序列判断井字棋游戏的结果。

    Args:
        moves: 一个二维列表，表示玩家A和B按顺序进行的移动。
               每个移动是一个包含两个整数的列表，分别表示行和列的索引（0-2）。

    Returns:
        str: 返回游戏结果，可能的值包括：
             "A" - 玩家A获胜
             "B" - 玩家B获胜
             "Draw" - 平局（棋盘已满且无人获胜）
             "Pending" - 游戏尚未结束（还有空位且无人获胜）
    """

    def tictactoe(self, moves: list[list[int]]) -> str:
        # 初始化3x3棋盘，0表示空位
        board = [[0] * 3 for _ in range(3)]
        player = 1  # 1代表玩家A，-1代表玩家B

        # 按照移动序列在棋盘上放置棋子，并切换玩家
        for move in moves:
            row, col = move
            board[row][col] = player
            player *= -1  # 切换玩家

        # 检查两条对角线是否形成胜利条件（和的绝对值为3表示同一玩家占据整条线）
        if abs(board[0][0] + board[1][1] + board[2][2]) == 3 or \
                abs(board[0][2] + board[1][1] + board[2][0]) == 3:
            # 根据中心位置的值判断获胜玩家（1为A，-1为B）
            return "A" if board[1][1] == 1 else "B"

        # 检查所有行和列是否形成胜利条件
        for i in range(3):
            if abs(board[i][0] + board[i][1] + board[i][2]) == 3 or \
                    abs(board[0][i] + board[1][i] + board[2][i]) == 3:
                # 根据对应位置的值判断获胜玩家
                return "A" if board[i][i] == 1 else "B"

        # 如果没有获胜者，根据移动次数判断是平局还是游戏未结束
        return "Draw" if len(moves) == 9 else "Pending"


# 复杂的很，题目我都看半天，官方的题解很复杂，这一版还好
# 2025.10.20


