# coding: utf-8
'''
给定一个整数矩阵，请找出一个子矩阵，
使得其数字之和等于0.输出答案时，请返回左上数字和右下数字的坐标。
样例
给定矩阵
[
  [1 ,5 ,7],
  [3 ,7 ,-8],
  [4 ,-8 ,9],
]
返回 [(1,1), (2,2)]
'''
class Solution:
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number
    def submatrixSum(self, matrix):
        lenM = len(matrix)
        lenN = len(matrix[0])
        if lenM == lenN == 1 and matrix[0][0] == 0:
            return [[0, 0], [0, 0]]
        f = [[0 for x in xrange(lenN + 1)] for y in xrange(lenM + 1)]

        for i in xrange(1, lenM + 1):
            for j in xrange(1, lenN + 1):
                f[i][j] = f[i - 1][j] + f[i][j - 1] - f[i - 1][j - 1] + matrix[i - 1][j - 1]
                for m in xrange(i):
                    for n in xrange(j):
                        if f[i][j] == f[i][n] - f[m][n] + f[m][j]:
                            return [[m, n], [i - 1, j - 1]]
solution = Solution()
print solution.submatrixSum([
  [1 ,5 ,7],
  [3 ,7 ,-8],
  [4 ,-8 ,9],
])
