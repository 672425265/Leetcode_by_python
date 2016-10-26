# coding: utf-8

'''
Given two binary strings, return their sum (also a binary string).
For example,
a = "11"
b = "1"
Return "100".
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len1, len2 = len(a) - 1, len(b) - 1
        carry = 0
        res = ""
        while len1 >= 0 or len2 >= 0:
            x = int(a[len1]) if len1 >= 0 else 0
            y = int(b[len2]) if len2 >= 0 else 0
            if (x + y + carry) % 2 == 0:
                res = '0' + res
            else:
                res = '1' + res
            carry = (x + y + carry) / 2
            len1, len2 = len1 - 1, len2 - 1
        if carry == 1:
            res = "1" + res
        return res

solution = Solution()
print solution.addBinary("1", "11")

