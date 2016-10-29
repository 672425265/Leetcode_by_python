# coding: utf-8
'''
Given a 2D binary matrix filled with 0's and 1's,
find the largest square containing only 1's
and return its area.
For example, given the following matrix:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        x_len = len(matrix)
        y_len = len(matrix[0])
        f = [[0] * y_len for i in range(x_len)]
        res = []
        for i in range(0, x_len):
            f[i][0] = int(matrix[i][0])
            res.append(f[i][0])
        for j in range(0, y_len):
            f[0][j] = int(matrix[0][j])
            res.append(f[0][j])
        for i in range(1, x_len):
            for j in range(1, y_len):
                if int(matrix[i][j]):
                    f[i][j] = min(f[i-1][j-1], f[i][j-1], f[i-1][j]) + 1
                res.append(f[i][j])
        return max(res)**2

solution = Solution()
str = ["0"]
print solution.maximalSquare(str)

