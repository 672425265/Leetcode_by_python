# coding: utf-8
'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids.
How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively
in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if m == 0 or n == 0:
            return 0
        sum = [([0] * n) for i in range((m))]
        for i in range(m):
            if obstacleGrid[i][0] != 1:
                sum[i][0] = 1
            else:
                sum[i][0] = 0
                break
        for j in range(n):
            if obstacleGrid[0][j] != 1:
                sum[0][j] = 1
            else:
                sum[0][j] = 0
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    sum[i][j] = sum[i - 1][j] + sum[i][j - 1]
                else:
                    sum[i][j] = 0
        return sum[m - 1][n - 1]

solution = Solution()
path = [
  [1,0,0],
  [0,1,0]
]
print solution.uniquePathsWithObstacles(path)