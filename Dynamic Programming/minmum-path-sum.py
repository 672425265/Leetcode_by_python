# coding: utf-8

'''
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes
the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        sum = [[0] * n for i in range(m)]

        sum[0][0] = grid[0][0]

        for i in xrange(1, m):
            sum[i][0] = sum[i-1][0] + grid[i][0]

        for j in xrange(1, n):
            sum[0][j] = sum[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                sum[i][j] = min(sum[i-1][j], sum[i][j-1]) + grid[i][j]

        return sum[m-1][n-1]

solution = Solution()
print solution.minPathSum([[1]])