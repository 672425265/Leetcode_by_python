# coding: utf-8
'''
You are climbing a stair case.
It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 1
        result = [1, 2]
        for i in range(n - 2):
            result.append(result[-2] + result[-1])
        return result[n-1]

solution = Solution()
print solution.climbStairs(4)