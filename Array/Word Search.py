# coding : utf-8

'''
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring.
The same letter cell may not be used more than once.
For example,
Given board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

class Solution(object):
    def find(self, board, i, j, word, start):
        if start == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[start]:
            return False
        board[i][j] = '#'
        rst = self.find(board, i-1, j, word, start+1) or self.find(board, i+1, j, word, start+1) \
              or self.find(board, i, j-1, word, start+1) or self.find(board, i, j+1, word, start+1)
        board[i][j] = word[start]
        return rst

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board is None or len(board) == 0:
            return False
        if len(word) == 0:
            return True
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == word[0]:
                    rst = self.find(board, i, j, word, 0)
                    if rst:
                        return True
        return False
