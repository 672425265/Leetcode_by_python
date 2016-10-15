# coding: utf-8

'''
A 2d grid map of m rows and n columns is
initially filled with water. We may perform
 an addLand operation which turns the water
 at position (row, col) into a land.
 Given a list of positions to operate,
 count the number of islands after each addLand operation.
 An island is surrounded by water
 and is formed by connecting adjacent lands horizontally
 or vertically. You may assume all four edges of
 the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water.
(Assume 0 represents water and 1 >represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid0 into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid0 into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid1 into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid2 into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
We return the result as an array: [1, 1, 2, 3]
'''

class Solution(object):
    def numIslands(self, m, n, positions):
        length = m * n
        # 表示各个index对应的root
        id = [-1] * length
        res = []
        # 记录island的数量
        count = 0
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for i in xrange(0, len(positions)):
            count += 1
            index = positions[i][0] * n + positions[i][1]
            # root初始化
            id[index] = index
            for j in xrange(0, len(dirs)):
                x = positions[i][0] + dirs[j][0]
                y = positions[i][1] + dirs[j][1]
                if x >= 0 and x < m and \
                                y >= 0 and y < n and \
                                id[x * n + y] != -1:
                    root = self.root(id, x * n + y)

                    # 发现root不等的情况下，才union, 同时减小count
                    if root != index:
                        id[root] = index
                        count -= 1
            res.append(count)
        return res

    def root(self, id, i):
        while i != id[i]:
            # 优化, 为了减小树的高度
            id[i] = id[id[i]]
            i = id[i]
        return i

solution = Solution()
print solution.numIslands(3, 3, [[0,0], [0,1], [1,2], [2,1]])