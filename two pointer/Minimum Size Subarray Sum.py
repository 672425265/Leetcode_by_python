# coding: utf-8
'''
Given an array of n positive integers and a positive integer s,
find the minimal length of a subarray of which the sum ≥ s.
If there isn't one, return 0 instead.
For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length
under the problem constraint.
'''
import sys

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 1 and nums[0] == s:
            return 1
        minlength = sys.maxint
        res = 0
        j = 0
        for i in range(0, length):
            while j < length and res < s:
               res += nums[j]
               j += 1
            if res >= s:
                minlength = min(minlength, j-i)
            res -= nums[i]
        if minlength == sys.maxint:
            return 0
        return minlength


solution = Solution()
nums1 = [2,3,1,2,4,3]
nums2 = [1]
nums3 = [1,2,3,4,5]
print solution.minSubArrayLen(5, nums1)


