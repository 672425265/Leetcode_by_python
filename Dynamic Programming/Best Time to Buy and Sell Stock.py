# coding: utf-8

'''
Say you have an array for which the ith element
is the price of a given stock on day i.

If you were only permitted to complete
at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5
(not 7-1 = 6, as selling price needs to
be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

'''
import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
            return 0
        profit = [0] * length
        for i in range(1, length):
            if prices[i] <= prices[i-1]:
                profit[i] = profit[i-1]
                continue
            else:
                profit[i] = prices[i] - min(prices[:i])
        return max(profit)

class Solution2(object):
    def maxProfit(self, prices):
        total = 0
        length = len(prices)
        if length == 0:
            return 0
        low = prices[0]
        for i in range(0, length):
            if prices[i] - low > total:
                total = prices[i] - low
            if prices[i] < low:
                low = prices[i]
        return total

solution = Solution2()
print solution.maxProfit([7,1,5,3,6,4])

