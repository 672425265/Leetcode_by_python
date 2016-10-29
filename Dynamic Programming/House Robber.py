# coding: utf-8

'''
You are a professional robber planning to rob houses along
a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them
is that adjacent houses have security system connected
and it will automatically contact the police
if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing
the amount of money of each house,
determine the maximum amount of money you
can rob tonight without alerting the police.
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if nums is None or length == 0:
            return 0
        ans = [0] * (length + 1)
        ans[0], ans[1] = 0, nums[0]
        for i in range(2, length + 1):
            ans[i] = max(ans[i - 1], ans[i - 2] + nums[i - 1])
        return ans[length]

solution = Solution()
print solution.rob([3,8,4,1])


