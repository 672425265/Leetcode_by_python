#coding: utf-8

'''
Given an array S of n integers, find three integers in S
such that the sum is closest to a given number, target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = None
        for i in xrange(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if ans is None or abs((sum - target)) < abs(ans - target):
                    ans = sum
                if sum <= target:
                    left += 1
                else:
                    right -= 1
        return ans