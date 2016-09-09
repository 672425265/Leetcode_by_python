# coding: utf-8
'''Given a rotated sorted array, recover
it to sorted array in-place.
Example [4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]
'''
class Solution:
    """
       @param nums: The rotated sorted array
       @return: nothing
    """
    def reverse(self, nums, start, end):
        i, j = start, end
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1

    def recoverRotatedSortedArray(self, nums):
        index = 0
        while index < len(nums) - 1:
            if nums[index] > nums[index+1]:
                self.reverse(nums, 0, index)
                self.reverse(nums, index + 1, len(nums)-1)
                self.reverse(nums, 0, len(nums) - 1)
                return
            index += 1

solution = Solution()
nums = [4,5,1,2,3]
solution.recoverRotatedSortedArray(nums)
print nums
