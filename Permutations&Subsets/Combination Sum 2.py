# coding: utf-8
'''
Given a collection of candidate numbers (C)
and a target number (T), find all unique combinations
in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''

class Solution(object):
    def helper(self, rst, solution, candidates, sum, index):

        if sum == 0:
            rst.append(solution + [])

        if index >= len(candidates) or sum < 0:
            return

        prev = -1
        for i in xrange(index, len(candidates)):
            if candidates[i] != prev:
                solution.append(candidates[i])
                self.helper(rst, solution, candidates, sum - candidates[i], i + 1)
                prev = candidates[i]
                solution.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rst = []
        if len(candidates) < 1:
            return rst
        solution = []
        candidates.sort()
        self.helper(rst, solution, candidates, target, 0)
        return rst

solution = Solution()
print solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)