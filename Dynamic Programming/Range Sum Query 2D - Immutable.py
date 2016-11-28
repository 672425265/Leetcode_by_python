# coding: utf-8

'''
Given a 2D matrix matrix, find the sum of the elements inside the rectangle
defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1)
and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
'''


class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        self.sums = [[0] * (n + 1) for x in range(m + 1)]
        for x in range(1, m+1):
            rowSum = 0
            for y in range(1, n+1):
                self.sums[x][y] += rowSum + matrix[x - 1][y - 1]
                if x > 1:
                    self.sums[x][y] += self.sums[x - 1][y]
                rowSum += matrix[x - 1][y - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sums[row2 + 1][col2 + 1] + self.sums[row1][col1] \
               - self.sums[row1][col2+1] - self.sums[row2+1][col1]

matrix = [[3,0,1,4,2], [5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
numMatrix = NumMatrix(matrix)
print numMatrix.sumRegion(2, 1, 4, 3)
print numMatrix.sumRegion(1, 2, 3, 4)