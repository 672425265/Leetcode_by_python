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

class Solution(object):
    def dfs(self, candidates, target, path, index, result):
        if target == 0:
            result.append(path + [])
            return

        prev = -1
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break
            # 去重
            if prev != -1 and prev == candidates[i]:
                continue
            path.append(candidates[i])
            self.dfs(candidates, target - candidates[i], path, i, result)
            path.pop()
            prev = candidates[i]

    def combinationSum(self, candidates, target):
        result = []
        if candidates is None:
            return None
        candidates.sort()
        path = []
        self.dfs(candidates, target, path, 0, result)
        return result

class Solution2:
    ret = []
    def combinationSum(self, candidates, target):
        candidates = list(set(candidates))
        candidates.sort()
        self.DFS(candidates, target, 0, [])
        return self.ret

    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0:
            return self.ret.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]])

solution = Solution2()
print solution.combinationSum([2,2,6,7], 6)