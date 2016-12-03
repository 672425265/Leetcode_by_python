# coding: utf-8

'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
'''

'''
若一个整数是4的幂，则其二进制形式具有如下特点：

1. 最高位为1，其余位为0

2. 0的个数为偶数

条件1可以用num & (num - 1) == 0判断

条件2可以用num & 0x55555555 > 0判断
'''

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num & (num - 1) == 0 and num & 0x55555555 > 0

class Solution2(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num & (num - 1) == 0 and (num - 1) % 3 == 0
