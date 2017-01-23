class Solution:
    # @param {int} dividend the dividend
    # @param {int} divisor the divisor
    # @return {int} the result
    def divide(self, dividend, divisor):
        # Write your code here
        if (dividend < 0) ^ (divisor < 0):
            sign = -1
        else:
            sign = 1
        dividend, divisor = abs(dividend), abs(divisor)
        if divisor == 0:
            return None
        result = 0
        while dividend >= divisor:
            i = 1
            tmp = divisor
            while dividend >= tmp:
                tmp = tmp << 1
                i += 1
            result += (1 << (i - 2))
            dividend -= (divisor << (i - 2))
        result *= sign
        if result > 2147483647:
            result = 2147483647
        return result