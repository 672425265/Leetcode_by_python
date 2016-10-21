# coding: utf-8

'''
水平面上有 N 座大楼，每座大楼都是矩阵的形状，
可以用三个数字表示 (start, end, height)，
分别代表其在x轴上的起点，终点和高度。大楼之间从远处看可能会重叠，
求出 N 座大楼的外轮廓线。

外轮廓线的表示方法为若干三元组，每个三元组包含三个数字 (start, end, height)，
代表这段轮廓的起始位置，终止位置和高度。

请注意合并同样高度的相邻轮廓，不同的轮廓线在x轴上不能有重叠。

样例
给出三座大楼：

[
  [1, 3, 3],
  [2, 4, 4],
  [5, 6, 1]
]
外轮廓线为：

[
  [1, 2, 3],
  [2, 4, 4],
  [5, 6, 1]
]
'''

import heapq

class Solution:
    # @param buildings: A list of lists of integers
    # @return: A list of lists of integers
    def buildingOutline(self, buildings):
        # write your code here
        if len(buildings) == 0:
            return []

        positions = set([b[0] for b in buildings] + [b[1] for b in buildings])
        heap = []
        result = [[-1, 0]]
        i = 0
        buildings_len = len(buildings)
        for pos in positions:
            while i < buildings_len and buildings[i][0] <= pos:
                heapq.heappush(heap, (-buildings[i][2], buildings[i][1]))
                i += 1
            while heap and heap[0][1] <= pos:
                heapq.heappop(heap)

            height = 0
            if heap != []:
                height = -heap[0][0]
            if height != result[-1][1]:
                result.append([pos, height])
        value = result[1:]
        return value

buildings = [
  [1, 3, 3],
  [2, 4, 4],
  [5, 6, 1]
]
'''
[
  [1, 2, 3],
  [2, 4, 4],
  [5, 6, 1]
]
'''
solution = Solution()
print solution.buildingOutline(buildings)