# coding: utf-8
'''
Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by
rotating the array A k positions clock-wise,
we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:
n is guaranteed to be less than 105.

Example:

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
'''


class Solution(object):
    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
        return nums

    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        if length == 0:
            return 0
        sum = [0] * length
        for i in xrange(0, length):
            value = 0
            B = A + []
            self.reverse(B, 0, length - i - 1)
            self.reverse(B, length - i, length - 1)
            self.reverse(B, 0, length - 1)
            for j in xrange(length):
                value += j * B[j]
            sum[i] = value
        return max(sum)

'''
F(0) = 0A + 1B + 2C +3D

F(1) = 0D + 1A + 2B +3C

F(2) = 0C + 1D + 2A +3B

F(3) = 0B + 1C + 2D +3A

那么，我们通过仔细观察，我们可以得出下面的规律：

F(1) = F(0) + sum - 4D

F(2) = F(1) + sum - 4C

F(3) = F(2) + sum - 4B

那么我们就找到规律了, F(i) = F(i-1) + sum - n*A[n-i]，

可以写出代码如下：
'''

class Solution2(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        t = 0
        sum = 0
        n = len(A)
        for i in xrange(n):
            sum += A[i]
            t += i * A[i]
        res = t
        for i in xrange(1, n):
            t = t + sum - n * A[n - i]
            res = max(res, t)
        return res

solution = Solution()
A = [4, 3, 2, 6]
print solution.maxRotateFunction(A)

