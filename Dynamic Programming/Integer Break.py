# coding: utf-8

'''
Given a positive integer n, break it into the sum of at least two positive integers
and maximize the product of those integers. Return the maximum product you can get.
For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
Note: You may assume that n is not less than 2 and not larger than 58.
'''

'''
解法II 动态规划

dp[i]表示整数i拆分可以得到的最大乘积，则dp[i]只与dp[i - 2], dp[i - 3]两个状态有关

得到状态转移方程：

dp[x] = max(3 * dp[x - 3], 2 * dp[x - 2])
'''

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n - 1
        dp = [0] * (n + 1)
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n + 1):
            dp[i] = max(3 * dp[i - 3], 2 * dp[i - 2])
        return dp[n]

solution = Solution()
print solution.integerBreak(5)