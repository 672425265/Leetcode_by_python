# coding: utf-8
'''
在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m，每个物品的大小为A[i]
样例
如果有4个物品[2, 3, 5, 7]
如果背包的大小为11，可以选择[2, 3, 5]装入背包，最多可以装满10的空间。
如果背包的大小为12，可以选择[2, 3, 7]装入背包，最多可以装满12的空间。
函数需要返回最多能装满的空间大小。
'''

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # f[i][S] : 前 i 个物品,取出一些能否组成和为S
        f = [[False] * (m+1) for i in range(len(A) + 1)]
        f[0][0] = True
        for i in range(1, len(A)+1):
            for j in range(0, m+1):
                f[i][j] = f[i - 1][j]
                if j >= A[i-1] and f[i-1][j - A[i-1]]:
                    f[i][j] = True

        for i in range(m, -1, -1):
            if f[len(A)][i]:
                return i

        return 0

class Solution2:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [0 for x in range(m+1)]
        dp[0] = 1
        ans = 0
        for item in A:
            for i in range(m,-1,-1):
                if i-item >=0 and dp[i-item] > 0:
                    ans = max(ans,i)
                    dp[i] = 1
        return ans
solution = Solution()
print solution.backPack(11,[2,3,5,7])