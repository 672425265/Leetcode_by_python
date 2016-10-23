# coding: utf-8

'''
Say you have an array for which the ith element
is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions
as you like (ie, buy one and
sell one share of the stock multiple times).
However, you may not engage in multiple transactions
at the same time (ie, you must sell the stock
before you buy again).

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 7
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(0, len(prices) - 1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                profit += diff
        return profit

solution = Solution()
print solution.maxProfit([7,1,5,3,6,4])