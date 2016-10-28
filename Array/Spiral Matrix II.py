# coding: utf-8

'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        res = [[0] * n for i in range(n)]
        left, right, bottom, top, num = 0, n - 1, n - 1, 0, 1
        while left < right and top < bottom:
            for i in range(left, right):
                res[top][i] = num
                num += 1
            for i in range(top, bottom):
                res[i][right] = num
                num += 1
            for i in range(right, left, -1):
                res[bottom][i] = num
                num += 1
            for i in range(bottom, top, -1):
                res[i][left] = num
                num += 1
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        if n % 2 == 1:
            res[n / 2][n / 2] = num
        return res

solution = Solution()
print solution.generateMatrix(1)


