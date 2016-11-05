# coding: utf-8

'''
You are given coins of different denominations
and a total amount of money amount. Write a function to compute
the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
'''


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [-1] * (amount + 1)
        res[0] = 0
        for i in range(0, amount + 1):
            if res[i] < 0:
                continue
            for c in coins:
                if i + c > amount:
                    continue
                if res[i + c] < 0 or res[i + c] > res[i] + 1:
                    res[i + c] = res[i] + 1
        return res[amount]

class Solution2(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [amount+1] * (amount + 1)
        res[0] = 0
        for i in range(1, amount+1):
            for j in range(0, len(coins)):
                if coins[j] <= i:
                    res[i] = min(res[i], res[i - coins[j]] + 1)
        if res[amount] > amount:
            return -1
        else:
            return res[amount]

coins = [370,417,408,156,143,434,168,83,177,280,117]
amount = 9953
solution = Solution()
print solution.coinChange(coins, amount)

