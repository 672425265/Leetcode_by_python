# coding: utf-8

'''
给定n个不同的正整数，整数k（k < = n）以及一个目标数字。　　　　
在这n个数里面找出K个数，使得这K个数的和等于目标数字，求问有多少种方案?
给出[1,2,3,4]，k=2， target=5，[1,4] and [2,3]是2个符合要求的方案
'''

class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        n = len(A)
        ans = [[[0 for i in range(target + 1)] for j in range(k + 1)] for K in range(n + 1)]
        ans[0][0][0] = 1
        for i in range(n):
            item = A[i]
            for j in range(target+1):
                for K in range(k+1):
                    tk = k - K
                    tj = target - j
                    ans[i+1][tk][tj] = ans[i][tk][tj]
                    if tk - 1 >= 0 and tj - item >= 0:
                        ans[i+1][tk][tj] += ans[i][tk-1][tj-item]
        return ans[n][k][target]

solution = Solution()
print solution.kSum([1,2,3,4], 2, 5)



