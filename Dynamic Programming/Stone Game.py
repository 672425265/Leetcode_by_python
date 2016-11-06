# coding: utf-8
'''
There is a stone game.At the beginning of the game the player picks n piles of stones in a line.
The goal is to merge the stones in one pile observing the following rules:
At each step of the game,the player can merge two adjacent piles to a new pile.
The score is the number of stones in the new pile.
You are to determine the minimum of the total score.
Example
For [4, 1, 1, 4], in the best solution, the total score is 18:
Merge second and third piles => [4, 2, 4], score +2
Merge the first two piles => [6, 4]，score +6
Merge the last two piles => [10], score +10
Other two examples:
1.  [1, 1, 1, 1] return 8
2.  [4, 4, 5, 9] return 43
'''

import sys

def stoneGame(A):
    if A is None or len(A) == 0:
        return 0
    n = len(A)

    sum = [[0] * n for i in range(n)]
    for i in range(n):
        sum[i][i] = A[i]
        for j in range(i+1, n):
            sum[i][j] = sum[i][j-1] + A[j]

    dp = [[0] * n for i in range(n)]
    for i in range(0, n):
        dp[i][i] = 0

    for l in range(2, n + 1):
        i = 0
        while i + l - 1 < n:
            j = i + l - 1
            minV = sys.maxint
            for k in range(i, j):
                minV = min(minV, dp[i][k] + dp[k+1][j])
            dp[i][j] = minV + sum[i][j]
            i += 1
    return dp[0][n-1]

A = [4, 4, 5, 9]
print stoneGame(A)
