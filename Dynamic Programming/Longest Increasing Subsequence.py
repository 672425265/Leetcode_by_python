# coding: utf-8
'''
Given an unsorted array of integers,
find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101],
therefore the length is 4.
Note that there may be more than one LIS combination,
it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = [0] * len(nums)
        max = 0
        for i in xrange(0, len(nums)):
            f[i] = 1
            for j in xrange(0, i):
                if nums[j] < nums[i]:
                    if f[i] <= f[j] + 1:
                        f[i] = f[j] + 1
            if f[i] > max:
                max = f[i]

        return max

solution = Solution()
print solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])