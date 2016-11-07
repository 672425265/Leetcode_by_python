# coding: utf-8
'''
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Follow up:
Could you do this in-place?
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0 or matrix is None:
            return
        length = len(matrix)
        for i in range(0, length/2):
            for j in range(0, (length+1)/2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[length - j - 1][i]
                matrix[length - j - 1][i] = matrix[length - i - 1][length - j - 1]
                matrix[length - i - 1][length - j - 1] = matrix[j][length - i - 1]
                matrix[j][length - i - 1] = tmp

class Solution2:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def rotate(self, matrix):
        # write your code here
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()