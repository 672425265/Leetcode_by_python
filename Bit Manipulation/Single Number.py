# coding: utf-8
'''
Given an array of integers, every element appears twice except for one.
Find that single one.
Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
'''

class Solution(object):
    '''
    对数组元素执行异或运算，最终结果即为所求。
    由于异或运算的性质，两个相同数字的异或等于0，而任意数字与0的亦或都等于它本身。
    另外，异或运算满足交换律。
    '''
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans ^= num
        return ans

solution = Solution()
print solution.singleNumber([2,2,5,3,3])
