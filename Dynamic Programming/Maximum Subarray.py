#coding: utf-8
'''
Find the contiguous subarray within
an array (containing at least one number)
which has the largest sum.
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if nums is None or length == 0:
            return 0
        res_loc = [0] * length
        res_global = [0] * length
        res_loc[0] = nums[0]
        res_global[0] = nums[0]
        for i in range(1, length):
            res_loc[i] = max(nums[i], res_loc[i-1]+nums[i])
            res_global[i] = max(res_loc[i], res_global[i-1])
        return res_global[length - 1]

solution = Solution()
print solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
