# coding: utf-8

'''
Given a set of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
'''

class Solution3(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if candidates is None:
            return res
        path = []
        candidates.sort()
        self.dfs(candidates, 0, target, path, res)
        return res

    def dfs(self, candidates, index, target, path, res):
        if target == 0:
            res.append([] + path)
            return
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break
            if i != index and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            self.dfs(candidates, i, target - candidates[i], path, res)
            path.pop()

solution = Solution3()
print solution.combinationSum([2,6,6,7], 6)