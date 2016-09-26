# coding: utf-8
import sys

'''
Given a triangle, find the minimum path sum from
top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
'''


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = [triangle[0]]
        N = len(triangle)
        for i in range(1, len(triangle)):
            res.append([])
            for j in range(len(triangle[i])):
                if j-1 >= 0 and j < len(triangle[i-1]):
                    res[i].append(min(res[i-1][j-1], res[i-1][j])
                                  + triangle[i][j])
                elif j-1 >= 0:
                    res[i].append(res[i-1][j-1]+triangle[i][j])
                else:
                    res[i].append(res[i-1][j]+triangle[i][j])
        minvalue = min(res[N-1])
        return minvalue

class Solution2(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle is None or len(triangle) == 0:
            return -1
        if triangle[0] is None or len(triangle[0]) == 0:
            return -1
        if len(triangle) == 1 and len(triangle[0]) == 1:
            return triangle[0][0]
        m = len(triangle)
        for i in range(m-2, -1, -1):
            for j in range(0, len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        minnum = triangle[0][0]
        return minnum


solution = Solution2()
print solution.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])