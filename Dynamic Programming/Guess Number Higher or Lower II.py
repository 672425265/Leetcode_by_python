# coding: utf-8

'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x.
You win the game when you guess
the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
'''

'''
状态转移方程：
dp[i][j] = min(k + max(dp[i][k - 1], dp[k + 1][j]))

那么我们需要建立一个二维的dp数组，其中dp[i][j]表示从数字i到j之间猜中任意一个数字最少需要花费的钱数，
那么我们需要遍历每一段区间[j, i]，维护一个全局最小值global_min变量，然后遍历该区间中的每一个数字，
计算局部最大值local_max = k + max(dp[j][k - 1], dp[k + 1][i])，这个正好是将该区间在每一个位置都分为两段，
然后取当前位置的花费加上左右两段中较大的花费之和为局部最大值，然后更新全局最小值，
最后在更新dp[j][i]的时候看j和i是否是相邻的，相邻的话赋为i，否则赋为global_min
'''
import sys

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for _ in range(n+1)]
        for gap in range(1, n):
            for lo in range(1, n+1-gap):
                hi = lo + gap
                dp[lo][hi] = min(x + max(dp[lo][x-1], dp[x+1][hi])
                                   for x in range(lo, hi))
        return dp[1][n]

class Solution2(object):
    def getMoneyAmount(self, n):
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(2, n+1):
            for j in range(i-1, 0, -1):
                global_min = sys.maxint
                for k in range(j+1, i):
                    local_max = k + max(dp[j][k - 1], dp[k + 1][i])
                    global_min = min(global_min, local_max)
                if j + 1 == i:
                    dp[j][i] = j
                else:
                    dp[j][i] = global_min
        return dp[1][n]

solution = Solution2()
print solution.getMoneyAmount(3)