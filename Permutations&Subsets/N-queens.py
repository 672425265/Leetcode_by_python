# coding: utf-8
'''
The n-queens puzzle is the problem of placing n queens on an
n×n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to
the n-queens puzzle.

Each solution contains a distinct board configuration
of the n-queens' placement, where 'Q' and '.'
both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:
'''
class Solution(object):

    def drawChessboard(self, cols):
        chessboard = [0 for i in cols]
        for i in xrange(0, len(cols)):
            chessboard[i] = ""
            for j in xrange(0, len(cols)):
                if j == cols[i]:
                    chessboard[i] += "Q"
                else:
                    chessboard[i] += "."

        return chessboard

    def isValid(self, cols, col):
        # 之前有多少行已经填了
        row = len(cols)
        # 枚举之前填过的行
        for i in xrange(0, row):
            # 如果他们在列上能互相攻击, 比如我们想放到第i行,第col列,若该列存在皇后,则返回False
            if cols[i] == col:
                return False
            # 我们尝试放到(row,col)的位置,
            if i - cols[i] == row - col:
                return False
            if i + cols[i] == row + col:
                return False
        return True

    def search(self, n, cols, result):
        # 把棋盘画出来
        if len(cols) == n:
            result.append(self.drawChessboard(cols))
            return
        # 选择要插入第几列
        for col in xrange(0, n):
            if not self.isValid(cols, col):
                continue
            cols.append(col)
            self.search(n, cols, result)
            cols.pop()

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        self.search(n, [], result)
        return result

solution = Solution()
print solution.solveNQueens(4)
