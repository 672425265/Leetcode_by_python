# coding: utf-8

'''
Given an array with n objects colored red,
white or blue, sort them so that objects of the same color
are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2
to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's
sort function for this problem.
'''


class Solution(object):
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None and len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                self.swap(nums, left, i)
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                self.swap(nums, right, i)
                right -= 1

solution = Solution()
nums = [1,0,1,0]
solution.sortColors(nums)
print nums

