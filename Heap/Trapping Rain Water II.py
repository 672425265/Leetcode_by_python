# coding: utf-8
'''
Given an m x n matrix of positive integers
representing the height of each unit cell in a 2D elevation map,
compute the volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit
cell is greater than 0 and is less than 20,000.
Example:
Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.
'''

'''
1. 从外面找最小值
扫一遍 o(n)
heap o(logn)

2. 向内灌水
'''

import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0

        m = len(heightMap)
        n = len(heightMap[0])
        heap = []
        visited = [[0] * n for i in range(0, m)]
        result = 0

        # 堆中存放的三元组,为了去重,因为每一外围可能会有相同的数字
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))
            visited[i][0] = 1
            visited[i][n-1] = 1

        for j in range(1, n):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m - 1][j], m - 1, j))
            visited[0][j] = 1
            visited[m - 1][j] = 1

        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]

        while heap:
            curr = heapq.heappop(heap)
            for x in range(4):
                nx = curr[1] + dx[x]
                ny = curr[2] + dy[x]

                if nx >= 0 and nx < m and ny >= 0 and ny < n and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    heapq.heappush(heap, (max(curr[0], heightMap[nx][ny]), nx, ny))
                    result += max(0, curr[0] - heightMap[nx][ny])

        return result


heightMap = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
soluton = Solution()
print soluton.trapRainWater(heightMap)