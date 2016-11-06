# coding: utf-8
'''
给出n个物品的体积A[i]和其价值V[i]，
将他们装入一个大小为m的背包，
最多能装入的总价值有多大？
A[i], V[i], n, m均为整数。你不能将物品进行切分。
你所挑选的物品总体积需要小于等于给定的m。
样例
对于物品体积[2, 3, 5, 7]和对应的价值[1, 5, 2, 4],
假设背包大小为10的话，最大能够装入的价值为9。
'''

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        # f[i][j]: 表示前 i 个物品当中选一些物品组成容量为 j 的最大价值
        res = [[0] * (m+1) for i in range(len(A)+1)]
        res[0][0] = 0
        for i in range(1, len(A) + 1):
            for j in range(0, m+1):
                if j - A[i-1] < 0:
                    res[i][j] = res[i-1][j]
                else:
                    res[i][j] = max(res[i-1][j-A[i-1]] + V[i-1], res[i-1][j])
        return res[len(A)][m]

solution = Solution()
print solution.backPackII(10,[2,2,5,7],[1,5,2,4])
