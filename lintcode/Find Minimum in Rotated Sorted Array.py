#coding: utf-8
'''
Suppose a sorted array is rotated at some pivot
unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
You may assume no duplicate exists in the array.
'''

class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        if len(nums) == 0:
            return 0

        start, end = 0, len(nums) - 1
        # target = nums[end]
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] <= nums[end]:
                end = mid
            else:
                start = mid
        return min(nums[start], nums[end])

    def findMin2(self, nums):
        if len(nums) == 0:
            return 0
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start+end)/2
            # if nums[mid] == nums[end]:
            #     end -= 1
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]

solution = Solution()
print solution.findMin([4,5,6,7,1,2,3])
