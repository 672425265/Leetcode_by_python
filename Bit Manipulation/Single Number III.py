# coding: utf-8
'''
Given an array of numbers nums, in which exactly two elements appear only once
and all the other elements appear exactly twice. Find the two elements that appear only once.
For example:
Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant space complexity?
'''

class Solution:
    def singleNumber(self, nums):
        xor = reduce(lambda x, y : x ^ y, nums)
        lowbit = xor & -xor
        a = b = 0
        for num in nums:
            if num & lowbit:
                a ^= num
            else:
                b ^= num
        return [a, b]

solution = Solution()
print solution.singleNumber([1, 2, 1, 3, 2, 5])