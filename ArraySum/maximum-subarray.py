# coding: utf-8

'''
给定一个整数数组，找到一个具有最大和的子数组，返回其最大和。
注意事项
子数组最少包含一个数
样例
给出数组[−2,2,−3,4,−1,2,1,−5,3]，
符合要求的子数组为[4,−1,2,1]，
其最大和为6
'''
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        n = len(nums)
        # 前 i 个元素, 连续子数组和最大
        Global = [0] * n
        # 以第 i 元素结尾的,连续最大子数组和
        Local = [0] * n
        Global[0] = nums[0]
        Local[0] = nums[0]
        for i in range(1, n):
            Local[i] = max(nums[i], Local[i-1] + nums[i])
            Global[i] = max(Local[i], Global[i-1])
        return Global[n-1]

solution = Solution()
nums = [-2,2,-3,4,-1,2,1,-5,3]
print solution.maxSubArray(nums)