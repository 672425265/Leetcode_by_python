# coding:utf-8
'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled,
where empty cells are filled with the character '.'.
A partially filled sudoku which is valid.
Note:
A valid Sudoku board (partially filled) is not necessarily solvable.
Only the filled cells need to be validated.
'''

class Solution(object):
    def process(self, visited, digit):
        if digit == ".":
            return True
        num = ord(digit) - ord("0")
        if num < 1 or num > 9 or visited[num-1] == True:
            return False
        visited[num-1] = True
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0, 9):
            visited = [False] * 9
            for j in range(0, 9):
                if not self.process(visited, board[i][j]):
                    return False

        for i in range(0, 9):
            visited = [False] * 9
            for j in range(0, 9):
                if not self.process(visited, board[j][i]):
                    return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                visited = [False] * 9
                for k in range(0, 9):
                    if not self.process(visited, board[i + k/3][j + k%3]):
                        return False
        return True


