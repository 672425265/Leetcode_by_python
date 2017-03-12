# coding: utf-8
'''
Find all possible combinations of k numbers that
add up to a number n,
given that only numbers from 1 to 9 can be
used and each combination should be a unique set of numbers.

Example 1:
Input: k = 3, n = 7
Output:
[[1,2,4]]
Example 2:
Input: k = 3, n = 9
Output:
[[1,2,6], [1,3,5], [2,3,4]]
'''

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        path = []
        res = []
        self.dfs(k, n, path, res, 1)
        return res

    def dfs(self, k, n, path, res, start):
        if n == 0 and k == 0:
            res.append([] + path)
            return
        for i in range(start, 10):
            if i > n:
                break
            path.append(i)
            self.dfs(k - 1, n - i, path, res, i + 1)
            path.pop()

solution = Solution()
print solution.combinationSum3(3, 10)