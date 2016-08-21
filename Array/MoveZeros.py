# -*- coding: utf-8 -*-
'''
Given an array nums, write a function to move all 0's
to the end of it while maintaining the relative order of
the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
1. You must do this in-place without making a copy of the array.
2. Minimize the total number of operations.
'''

class Solution(object):
    def moveZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        pos = 0
        for item in nums:
            if item != 0:
                nums[pos] = item
                pos += 1
        while pos < len(nums):
            nums[pos] = 0
            pos += 1

'''
Test:
nums: [0,1,0,2,3,0]
'''

solution = Solution()
nums = [0, 1, 0, 2, 3, 0]
solution.moveZeros(nums)
print nums




