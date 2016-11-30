# coding: utf-8
'''
Calculate the sum of two integers a and b,
but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
'''

'''
用异或算不带进位的和，用与并左移1位来算进位，然后把两者加起来即可
'''
import sys

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        max_int = sys.maxint
        min_int = -1 * sys.maxint
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= max_int else ~((a % min_int) ^ max_int)


solution  = Solution()
print solution.getSum(-1, 1)