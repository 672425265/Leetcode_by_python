# coding: utf-8
'''
Given an 2D board, count how many different battleships are in it.
The battleships are represented with 'X's,
empty slots are represented with '.'s. You may assume the following rules:

You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words,
they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column),
where N can be of any size.
At least one horizontal or vertical cell separates between two battleships -
there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive -
as battleships will always have a cell separating between them.
'''

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        h = len(board)
        w = len(board[0]) if h else 0

        ans = 0
        for x in range(h):
            for y in range(w):
                if board[x][y] == "X":
                    if x > 0 and board[x-1][y] == "X":
                        continue
                    if y > 0 and board[x][y-1] == "X":
                        continue
                    ans += 1
        return ans

class Solution2(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        vs = set()
        h = len(board)
        w = len(board[0]) if h else 0

        def dfs(x, y):
            for dx, dy in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w:
                    if (nx, ny) not in vs and board[nx][ny] == 'X':
                        vs.add((nx, ny))
                        dfs(nx, ny)

        ans = 0
        for x in range(h):
            for y in range(w):
                if (x, y) not in vs and board[x][y] == 'X':
                    ans += 1
                    vs.add((x, y))
                    dfs(x, y)
        return ans