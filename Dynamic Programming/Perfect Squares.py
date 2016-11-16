# coding: utf-8
'''
Given a positive integer n, find the least number of
perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
For example, given n = 12, return 3 because 12 = 4 + 4 + 4;
given n = 13, return 2 because 13 = 4 + 9.
'''
import collections

class Solution:
    def numSquares(self, n):
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4

        for i in xrange(n+1):
            temp = i * i
            if temp <= n:
                if int((n - temp)**0.5) ** 2 + temp == n:
                    return 1 + (0 if temp == 0 else 1)
            else:
                break
        return 3