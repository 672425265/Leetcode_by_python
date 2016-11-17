# coding: utf-8

'''
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions
as you like (ie, buy one and sell one share of the stock multiple times)
with the following restrictions:
You may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:
prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
'''
'''
引入辅助数组sells和buys
sells[i]表示在第i天卖出股票所能获得的最大累积收益
buys[i]表示在第i天买入股票所能获得的最大累积收益
初始化令sells[0] = 0，buys[0] = -prices[0]
第i天交易时获得的累计收益只与第i-1天与第i-2天有关
记第i天与第i-1天的价格差：delta = price[i] - price[i - 1]
状态转移方程为：
sells[i] = max(buys[i - 1] + prices[i], sells[i - 1] + delta)
buys[i] = max(sells[i - 2] - prices[i], buys[i - 1] - delta)
上述方程的含义为：
第i天卖出的最大累积收益 = max(第i-1天买入~第i天卖出的最大累积收益, 第i-1天卖出后反悔~改为第i天卖出的最大累积收益)
第i天买入的最大累积收益 = max(第i-2天卖出~第i天买入的最大累积收益, 第i-1天买入后反悔~改为第i天买入的最大累积收益)
而实际上：
第i-1天卖出后反悔，改为第i天卖出 等价于 第i-1天持有股票，第i天再卖出
第i-1天买入后反悔，改为第i天买入 等价于 第i-1天没有股票，第i天再买入
所求的最大收益为max(sells)。显然，卖出股票时才可能获得收益。
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if prices is None or length == 0:
            return 0
        sells, buys = [0] * length, [0] * length
        sells[0], buys[0] = 0, -prices[0]
        for i in range(1, length):
            delta = prices[i] - prices[i-1]
            sells[i] = max(buys[i-1] + prices[i], sells[i-1] + delta)
            buys[i] = max(sells[i-2] - prices[i], buys[i-1] - delta)
        return max(sells)

solution = Solution()
print solution.maxProfit([1,2,3,0,2])