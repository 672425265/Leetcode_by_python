# coding: utf-8
'''
Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands. An island is surrounded
by water and is formed by connecting adjacent
lands horizontally or vertically.
You may assume all four edges of the grid
are all surrounded by water.

Example 1:
11110
11010
11000
00000
Answer: 1

Example 2:
11000
11000
00100
00011
Answer: 3
'''

'''
transformation
如果有一个 m 维矩阵
(x, y) => x * m + y : 1d
x = 1d / m
y = 1d % m
'''
class Solution(object):
    m, n = None, None
    def dfs(self, grid, i, j):
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return
        if grid[i][j] == "1":
            grid[i] = grid[i][:j] + '0' + grid[i][j + 1:]
            self.dfs(grid, i-1, j)
            self.dfs(grid, i+1,j)
            self.dfs(grid, i, j-1)
            self.dfs(grid, i, j+1)
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.m = len(grid)
        self.n = len(grid[0])
        if self.m == 0 or self.n == 0:
            return 0
        ans = 0
        for i in xrange(self.m):
            for j in xrange(self.n):
                if grid[i][j] == "0":
                    continue
                ans += 1
                self.dfs(grid, i, j)
        return ans


solution = Solution()
value = ["10000","11010","11000","00000"]
print solution.numIslands(value)


