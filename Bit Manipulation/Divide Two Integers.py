# coding: utf-8

'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''

'''
这个我们就得使用位运算。我们知道任何一个整数可以表示成以2的幂为底的一组基的线性组合,
即num=a_0*2^0+a_1*2^1+a_2*2^2+...+a_n*2^n
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        sign = 1
        if dividend >= 0 and divisor < 0 or dividend <= 0 and divisor > 0:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        current = divisor
        currentResult = 1
        while current <= dividend:
            current <<= 1
            currentResult <<= 1
        while divisor <= dividend:
            current >>= 1
            currentResult >>= 1
            if current <= dividend:
                dividend -= current
                result += currentResult
        return min(sign * result, MAX_INT)


solution = Solution()
print solution.divide(10, 5)