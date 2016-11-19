# coding: utf-8
'''
Given a m x n matrix, if an element is 0,
set its entire row and column to 0. Do it in place.
'''

'''
我们看到其实判断某一项是不是0只要看它对应的行或者列应不应该置0就可以，
所以我们可以维护一个行和列的布尔数组，
然后扫描一遍矩阵记录那一行或者列是不是应该置0即可，
后面赋值是一个常量时间的判断。这种方法的空间复杂度是O(m+n)。
其实还可以再优化，我们考虑使用第一行和第一列来记录上面所说的行和列的置0情况，
这里问题是那么第一行和第一列自己怎么办？想要记录它们自己是否要置0，
只需要两个变量（一个是第一行，一个是第一列）就可以了。然后就是第一行和第一列，
如果要置0，就把它的值赋成0（反正它最终也该是0，无论第一行或者第一列有没有0），
否则保留原值。然后根据第一行和第一列的记录对其他元素进行置0。
最后再根据前面的两个标记来确定是不是要把第一行和第一列置0就可以了。
这样的做法只需要两个额外变量，所以空间复杂度是O(1)。
'''

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        rownum = len(matrix)
        column = len(matrix[0])
        row = [False for i in range(rownum)]
        col = [False for i in range(column)]

        for i in range(rownum):
            for j in range(column):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        for i in range(rownum):
            for j in range(column):
                if row[i] or col[j]:
                    matrix[i][j] = 0
