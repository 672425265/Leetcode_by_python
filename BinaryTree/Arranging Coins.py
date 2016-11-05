# coding: utf-8
'''
You have a total of n coins that you want to form
in a staircase shape,
where every k-th row must have exactly k coins.
Given n, find the total number of full staircase rows
that can be formed.
n is a non-negative integer and fits within the range of a 32-bit signed integer.
Example 1:
n = 5
The coins can form the following rows:
¤
¤ ¤
¤ ¤
Because the 3rd row is incomplete, we return 2.
Example 2:
n = 8
The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
Because the 4th row is incomplete, we return 3.
'''
import math

class Solution2(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(2 * n + 0.25) - 0.5)

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while l <= r:
            m = (l + r) / 2
            if m*(m+1)/2 > n:
                r = m - 1
            else:
                l = m + 1
        return r

solution = Solution()
print solution.arrangeCoins(5)