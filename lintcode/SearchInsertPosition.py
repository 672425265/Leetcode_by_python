# coding: utf-8
'''
Given a sorted array and a target value,
return the index if the target is found. If not,
return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start = 0
        end = len(nums) - 1
        if target < nums[0]:
            return 0
        # find the last number less than target
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
        if nums[end] == target:
            return end
        if nums[end] < target:
            return end + 1
        if nums[start] == target:
            return start
        else:
            return start + 1

class Solution2(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start = 0
        end = len(nums) - 1
        if target > nums[end]:
            return end + 1
        # find the first number more than target
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end

solution = Solution()
solution2 = Solution2()
ans = solution.searchInsert([1,1,1,1,3], 1)
ans2 = solution2.searchInsert([1,1,1,1,3], 1)
print ans
print ans2

