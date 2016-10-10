# coding: utf-8

'''
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
UPDATE (2016/2/13):
The return format had been changed to zero-based indices.
Please read the above updated description carefully.
'''

'''
Idea:

if (考虑A[i]和A[j]满足某个条件)
    j--;
    do something
else if (考虑A[i]和A[j]不满足某个条件)
    i++;
    do something
else
    do something
    i++ or j--
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hashmap 存放nums中每个值出现的位置
        hashmap = dict()
        for i in xrange(0, len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = i
        return [-1, -1]
