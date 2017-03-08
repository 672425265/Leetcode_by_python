# coding: utf-8

'''
给定一个整数数组，找到和为零的子数组。
你的代码应该返回满足要求的子数组的起始位置和结束位置
样例
给出 [-3, 1, 2, -3, 4]，返回[0, 2] 或者 [1, 3].
'''

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        hs = {0:-1}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum in hs:
                return [hs[sum] + 1, i]
            hs[sum] = i
        return

solution = Solution()
print solution.subarraySum([-6, 1, 2, -3, 4])