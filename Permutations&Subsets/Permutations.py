# coding: utf-8

'''
Given a collection of distinct numbers,
return all possible permutations.
For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        path = []
        if nums is None or len(nums) == 0:
            return result
        self.subsetshelper(path, nums, result)
        return result

    def subsetshelper(self, list, nums, result):
        if len(list) == len(nums):
            result.append([] + list)
        for i in xrange(0, len(nums)):
            if nums[i] in list:
                continue
            list.append(nums[i])
            self.subsetshelper(list, nums, result)
            list.pop()

solution = Solution()
print solution.permute([1, 2, 3])
