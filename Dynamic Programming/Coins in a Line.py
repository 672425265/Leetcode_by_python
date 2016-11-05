# coding: utf-8
'''
There are n coins in a line.
Two players take turns to take one or two coins
from right side until there are no more coins left.
The player who take the last coin wins.
Could you please decide the first play will win or lose?

n = 1, return true.
n = 2, return true.
n = 3, return false.
n = 4, return true.
n = 5, return true.
'''
class Solution:
    def firstWillWin(self, n):
        res = [False] * (n+1)
        if n == 0:
            return False
        elif n == 1:
            return True
        elif n == 2:
            return True
        elif n == 3:
            return False
        elif n == 4:
            return True
        res[1] = True
        res[2] = True
        res[3] = False
        res[4] = True
        for i in range(5, n+1):
            res[i] = (res[i-2] and res[i-3]) \
                     or (res[i-3] and res[i-4])
        return res[n]

solution = Solution()
print solution.firstWillWin(100)
