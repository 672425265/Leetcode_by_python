# coding: utf-8

'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''

"""
尽可能地把数组中不大于n（n为数组长度）的正整数放置到下标+1与其数值相同的位置上

第一个下标+1与数值不同的数字，即为所求。

例如数组nums = [3,4,-1,1]，调整位置后的结果为：[1,-1,3,4]

除第二个数字外，其余数字均满足nums[i] = i + 1，因此返回2
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] < n and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1

solution = Solution()
print solution.firstMissingPositive([3,4,-1,1])