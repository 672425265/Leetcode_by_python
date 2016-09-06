'''
Binary search is a famous question in algorithm.
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity. If the target number does not exist in the array, return -1. Example If the array is [1, 2, 3, 3, 4, 5, 10],
for given target 3, return 2.
'''

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
         if len(nums) == 0:
             return -1
         end = len(nums) - 1
         start = 0
         while start < end - 1:
             mid = start + (end - start) / 2
             if nums[mid] == target:
                 end = mid
             elif nums[mid] < target:
                 start = mid
             elif nums[mid] > target:
                 end = mid
         if (nums[start] == target):
             return start
         if (nums[end] == target):
             return end
         return -1

solution = Solution()
ans  = solution.binarySearch([1,2,2,1], 1)
print ans