# coding: utf-8
'''
Given two integers n and k, return all possible
combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

class Solution(object):
    def helper(self, rst, solution, n, k, start):
        if len(solution) == k:
            rst.append(solution + [])
            return
        # we can stop much earlier if I notice that the number of remaining elements
        # is smaller than needed to fill combination
        if n - start + 1 < k - len(solution):
            return
        
        for i in xrange(start, n + 1):
            solution.append(i)
            self.helper(rst, solution, n, k, i + 1)
            solution.pop()

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        rst = []
        solution = []
        self.helper(rst, solution, n, k, 1)
        return rst

solution = Solution()
print solution.combine(3, 2)
