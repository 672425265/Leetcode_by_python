# coding: utf-8

'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

样例
给定 [1,2,3] 表示 123, 返回 [1,2,4].

给定 [9,9,9] 表示 999, 返回 [1,0,0,0].
'''

class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        length = len(digits)
        num = 0
        index = 0
        for i in range(length - 1, -1, -1):
            num += digits[i] * 10 ** index
            index += 1
        num += 1
        ans = []
        for i in str(num):
            ans.append(int(i))
        return ans


class Solution2:
    def plusOne(self, digits):
        digits = list(reversed(digits))
        digits[0] += 1
        i, carry = 0, 0
        while i < len(digits):
            next_carry = (digits[i] + carry) / 10
            digits[i] = (digits[i] + carry) % 10
            i, carry = i + 1, next_carry
        if carry > 0:
            digits.append(carry)

        return list(reversed(digits))

solution = Solution2()
print solution.plusOne([1, 9, 9])
