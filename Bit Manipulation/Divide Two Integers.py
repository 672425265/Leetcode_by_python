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
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX
        neg = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
        a, b = abs(dividend), abs(divisor)
        ans, shift = 0, 31
        while shift >= 0:
            if a >= b << shift:
                a -= b << shift
                ans += 1 << shift
            shift -= 1
        if neg:
            ans -= ans
        if ans > INT_MAX:
            return INT_MAX
        return ans

solution = Solution()
print solution.divide(10, 2)