# coding: utf-8

'''
After robbing those houses on that street,
the thief has found himself a new place for his thievery
so that he will not get too much attention.
This time, all houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, the security system
for these houses remain the same as for those in
the previous street.
Given a list of non-negative integers representing
the amount of money of each house, determine
the maximum amount of money you can rob tonight
without alerting the police.
'''

class Solution(object):
    def rob(self, nums):
        length = len(nums)
        if nums is None or length == 0:
            return 0
        if length == 1:
            return nums[0]
        return max(self.robLinear(nums[1:]), self.robLinear(nums[:length-1]))

    def robLinear(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        ans = [0] * (length + 1)
        ans[0], ans[1] = 0, nums[0]
        for i in range(2, length + 1):
            ans[i] = max(ans[i - 1], ans[i - 2] + nums[i - 1])
        return ans[length]

solution = Solution()
print solution.rob([1,1,1])
