# coding: utf-8
'''
Given a collection of numbers that might contain
duplicates, return all possible unique permutations.
For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        if nums is None or len(nums) == 0:
            return result
        nums.sort()
        visit = [0 for i in range(len(nums))]
        for i in xrange(0, len(nums)):
            visit[i] = 0
        self.subsetshelper([], nums, visit, result)
        return result

    def subsetshelper(self, list, nums, visit, result):
        if len(list) == len(nums):
            result.append([] + list)
        for i in xrange(0, len(nums)):
            if visit[i] == 1\
                    or (i != 0 and nums[i] == nums[i-1] and visit[i-1] == 0):
                continue
            visit[i] = 1
            list.append(nums[i])
            self.subsetshelper(list, nums, visit, result)
            list.pop()
            visit[i] = 0

solution = Solution()
print solution.permuteUnique([3,3,0,3])