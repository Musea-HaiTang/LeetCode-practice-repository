"""
1041. 困于环中的机器人(中等)
在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。
北方向 是y轴的正方向。
南方向 是y轴的负方向。
东方向 是x轴的正方向。
西方向 是x轴的负方向。
机器人可以接受下列三条指令之一："G"：直走 1 个单位；"L"：左转 90 度；"R"：右转 90 度。
机器人按顺序执行指令 instructions，并一直重复它们。
只有在平面中存在环使得机器人永远无法离开时，返回 true。
否则，返回 false。
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direcIndex = 0
        x, y = 0, 0
        for instruction in instructions:
            if instruction == 'G':
                x += direc[direcIndex][0]
                y += direc[direcIndex][1]
            elif instruction == 'L':
                direcIndex -= 1
                direcIndex %= 4
            else:
                direcIndex += 1
                direcIndex %= 4
        return direcIndex != 0 or (x == 0 and y == 0)

# 这道题难在如何判断机器人是否在循环，尤其是一次操作后不在原点的情况
# 判断依据：机器人想要摆脱循环，在一串指令之后的状态，必须是不位于原点且方向朝北。

# 这个是题解思路的网站：
# https://leetcode.cn/problems/robot-bounded-in-circle/solutions/2217873/kun-yu-huan-zhong-de-ji-qi-ren-by-leetco-kjya/?envType=study-plan-v2&envId=programming-skills
#2025.11.6