# coding: utf-8
'''
有 n 个不同价值的硬币排成一条线。两个参赛者轮流从左边
依次拿走 1 或 2 个硬币，直到没有硬币为止。计算两个人分别拿到的硬币总价值，
价值高的人获胜。
请判定 第一个玩家 是输还是赢？
给定数组 A = [1,2,2], 返回 true.
给定数组 A = [1,2,4], 返回 false.
'''

# res[n]: 现在还剩n个硬币,现在先手取硬币的人最后最多取的硬币价值总量
class Solution:
    def firstWillWin(self, values):
        length = len(values)
        if length < 3:
            return True
        res = [0] * (length + 1)
        res[0] = 0
        res[1] = values[length-1]
        res[2] = values[length-2] + values[length-1]
        res[3] = values[length-3] + values[length-2]
        for i in range(4, length + 1):
            res[i] = max(min(res[i-2],res[i-3])+values[length-i],
                         min(res[i-3],res[i-4])+values[length-i]+values[length-i+1])
        if res[length] > sum(values)/2:
            return True
        else:
            return False

solution = Solution()
A = [1,2]
print solution.firstWillWin(A)
