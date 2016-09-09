# coding: utf-8

'''
Suppose a sorted array is rotated at some pivot unknown
to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
The array may contain duplicate
'''


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start + 1< end:
            mid = (start+end)/2
            if nums[mid] == nums[end]:
                end -= 1
            elif nums[mid] < nums[end]:
                end = mid
            else:
                start = mid
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]