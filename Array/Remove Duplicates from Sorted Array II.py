# coding: utf-8
'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        prev = 1
        curr = 2
        while curr < len(nums):
            if nums[curr] == nums[prev] and nums[curr] == nums[prev-1]:
                curr += 1
            else:
                prev += 1
                nums[prev] = nums[curr]
                curr += 1
        return prev + 1