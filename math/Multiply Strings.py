# coding: utf-8

'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.
'''


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1, len2 = len(num1), len(num2)
        len3 = len1 + len2
        num3 = [0] * len3
        for i in range(len1 - 1, -1, -1):
            carry = 0
            j = len2 - 1
            while j >= 0:
                product = carry + num3[i + j + 1] + int(num1[i]) * int(num2[j])
                num3[i + j + 1] = product % 10
                carry = product / 10
                j -= 1
            num3[i + j + 1] = carry
        sb = ""
        i = 0
        while i < len3 - 1 and num3[i] == 0:
            i += 1
        while i < len3:
            sb += str(num3[i])
            i += 1
        return sb

solution = Solution()
print solution.multiply("8","8")


