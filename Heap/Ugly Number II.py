#coding: utf-8
'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers
whose prime factors only include 2, 3, 5.
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.
'''

import heapq

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n

        n -= 1
        key = [2, 3, 5]
        h = []
        for i in range(3):
            heapq.heappush(h, (key[i], i))
        value = key[0]
        while n > 0:
            value, level = heapq.heappop(h)
            while level < 3:
                new_value = key[level] * value
                heapq.heappush(h, (new_value, level))
                level += 1
            n -= 1
        return value

class Solution2(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglys = []
        uglys.append(1)
        p2, p3, p5 = 0, 0, 0

        for i in xrange(1, n):
            lastNumber = uglys[i-1]
            while uglys[p2] * 2 <= lastNumber:
                p2 += 1
            while uglys[p3] * 3 <= lastNumber:
                p3 += 1
            while uglys[p5] * 5 <= lastNumber:
                p5 += 1
            uglys.append(min(uglys[p2] * 2, uglys[p3] * 3, uglys[p5] * 5))

        return uglys[n - 1]

solution = Solution2()
print solution.nthUglyNumber(10)