# coding: utf-8

'''
Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets
such that the sum of elements in both subsets is equal.
Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:
Input: [1, 5, 11, 5]
Output: true

Explanation: The array can be partitioned
as [1, 5, 5] and [11].
Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned
into equal sum subsets.
'''

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        list_sum = sum(nums)
        if list_sum % 2 == 1:
            return False
        target = list_sum / 2
        dp = [False] * (target + 1)
        dp[0] = True
        for i in range(0, len(nums)):
            j = target
            while j >= nums[i]:
                dp[j] = dp[j] or dp[j - nums[i]]
                j -= 1
        return dp[target]

class Solution3(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        possible_sums = {0}
        for n in nums:
            possible_sums.update({(v + n) for v in possible_sums})
        return (sum(nums) / 2.)  in possible_sums

solution = Solution3()
print solution.canPartition([1,5,11,5])