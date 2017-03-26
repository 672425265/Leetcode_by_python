# coding: utf-8

'''
Given an array of integers, find how many pairs in the array such that
their sum is bigger than a specific target number. Please return the number
of pairs

Example:
Given nums = [2, 7, 11, 15], target = 24,
return 1.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = 0
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] == target:
                ans += 1
                right -= 1
            else:
                left += 1
        return ans

solution = Solution()  
print solution.twoSum([2, 7, 7, 15], 9)

