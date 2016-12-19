#coding: utf-8

'''
There is a list of sorted integers from 1 to n. Starting from left to right,
remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left,
remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left,
until a single number remains.

Find the last number that remains starting with a list of length n.

Example:
Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
'''
'''
根据题设要求的数字移除过程，可以发现每执行完一趟数字移除操作，
列表中剩余相邻数字之间的差都会加倍。
因此解决问题的关键就是找到每一趟数字消除操作之后剩余数字的起点。
'''

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = p = 1
        cnt = 0
        while n > 1:
            n /= 2
            cnt += 1
            p *= 2
            if cnt % 2:
                a += p / 2 + p * (n - 1)
            else:
                a -= p / 2 + p * (n - 1)
        return a

solution = Solution()
print solution.lastRemaining(9)