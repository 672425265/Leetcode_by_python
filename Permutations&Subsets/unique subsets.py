# coding: utf-8
'''
Given a collection of integers that might contain duplicates,
nums, return all possible subsets.
Note: The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if nums is None or len(nums) == 0:
            return result
        nums.sort()
        self.subsetshelper([], nums, 0, result)
        return result

    def subsetshelper(self, list, nums, pos, result):
        result.append([] + list)
        for i in xrange(pos, len(nums)):
            if i != pos and nums[i] == nums[i-1]:
                continue
            list.append(nums[i])
            self.subsetshelper(list, nums, i + 1, result)
            list.pop()

solution = Solution()
print solution.subsets([1,2,2])