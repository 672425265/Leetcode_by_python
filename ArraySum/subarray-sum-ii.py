# coding: utf-8
'''
Given an integer array, find a subarray where the sum of numbers is between two given interval. Your code should
return the number of possible answer.
Example
Given [1,2,3,4] and interval = [1,3], return 4.
The possible answers are:
[0, 0]
[0, 1]
[1, 1]
[3, 3]
'''

class Solution:
    def subarraySum(self, nums, start, end):
        ret = 0
        for i in range(0, len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum >= start and sum <= end:
                    ret += 1
        return ret

solution = Solution()
print solution.subarraySum([1,2,3,4], 1, 3)


