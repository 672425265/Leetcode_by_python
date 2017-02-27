# coding: utf-8

class Solution(object):
    def numOfZero(self, n):
        cnt = 0
        while n > 0:
            cnt += (n / 5)
            n /= 5
        return cnt

a = Solution()
print a.numOfZero(5)