# coding: utf-8

'''
Given an array of non-negative integers,
you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length
at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

Subscribe to see which companies asked this question
'''


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        can = [False]*len(nums)
        can[0] = True
        for i in xrange(1, len(nums)):
            for j in xrange(0, i):
                if can[j] and j + nums[j] >= i:
                    can[i] = True
                    break

        return can[len(nums) - 1]

class Solution2(object):
    def canJump(self, nums):
        p = 0
        ans = 0
        for item in nums[:-1]:
            ans = max(ans, p + item)
            if ans <= p:
                return False
            p += 1
        return True

solution = Solution2()
print solution.canJump([2,3,1,1,4])