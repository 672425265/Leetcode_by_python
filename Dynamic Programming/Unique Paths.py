# coding: utf-8
'''
A robot is located at the top-left corner
of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right
at any point in time. The robot is trying to
reach the bottom-right corner of the grid
(marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        sum = [([0] * n) for i in range((m))]
        for i in range(m):
            sum[i][0] = 1
        for j in range(n):
            sum[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                sum[i][j] = sum[i - 1][j] + sum[0][j - 1]
        return sum[m - 1][n - 1]


solution = Solution()
print solution.uniquePaths(2, 2)
