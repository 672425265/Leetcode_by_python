# coding: utf-8

'''
Given a sorted array of integers,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity
must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            left = start
        elif nums[end] == target:
            left = end
        else:
            return [-1, -1]

        start, end = left, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            right = end
        else:
            right = start
        return [left, right]

solution = Solution()
ans = solution.searchRange([1, 3, 3, 1], 3)
print ans