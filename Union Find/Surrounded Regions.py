# coding: utf-8

'''
Given a 2D board containing 'X' and 'O' (the letter O),
capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's
in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''

class Solution(object):
    rows = 0
    cols = 0
    board = [[0] * cols for i in xrange(rows)]
    queue = []

    def enqueue(self, x, y):
        if x >= 0 and x < self.rows and y >=0 and y < self.cols and self.board[x][y] == 'O':
            self.queue.append(x * self.cols + y)


    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

        for i in xrange(self.rows):
            self.enqueue(i, 0)
            self.enqueue(i, self.cols - 1)
        for j in xrange(1, self.cols - 1):
            self.enqueue(0, j)
            self.enqueue(self.rows - 1, j)

        while len(self.queue) > 0:
            cur = self.queue.pop()
            x = cur / self.cols
            y = cur % self.cols

            if board[x][y] == "O":
                board[x] = list(board[x])
                board[x][y] = "D"

            self.enqueue(x - 1, y)
            self.enqueue(x + 1, y)
            self.enqueue(x, y - 1)
            self.enqueue(x, y + 1)

        for i in xrange(0, self.rows):
            for j in xrange(0, self.cols):
                if board[i][j] == "D":
                    board[i] = list(board[i])
                    board[i][j] = "O"
                    board[i] = "".join(board[i])
                elif board[i][j] == "O":
                    board[i] = list(board[i])
                    board[i][j] = "X"
                    board[i] = "".join(board[i])

        self.queue = None
        self.board = None
        self.rows = 0
        self.cols = 0



nums = ["XXXX","XOOX","XXOX","XOXX"]

solution = Solution()
solution.solve(nums)
print nums



