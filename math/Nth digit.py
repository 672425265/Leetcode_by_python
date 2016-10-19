# coding: utf-8
'''
Find the nth digit of the infinite integer sequence 1, 2, 3, 4,
5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit
signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7,
8, 9, 10, 11, ...
is a 0, which is part of the number 10.
'''


'''
解题思路：
将整数序列划分为下列区间：

1   1-9
2   10-99
3   100-999
4   1000-9999
5   10000-99999
6   100000-999999
7   1000000-9999999
8   10000000-99999999
9   100000000-99999999
然后分区间求值即可。
'''

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        len, cnt, start = 1, 9, 1
        while n > len * cnt:
            n -= len * cnt
            # 变量len记录当前循环区间数字的位数
            len += 1
            # 每个长度的数字对应的个数: 比如长度为2的数字出现的次数
            cnt *= 10
            # 变量start用来记录当前循环区间的第一个数字
            start *= 10
        # 当n落到某一个确定的区间里了，
        # 那么(n-1)/len就是目标数字在该区间里的坐标
        start += (n-1) / len
        t = str(start)
        return ord(t[(n-1) % len]) - ord('0')


solution = Solution()
print solution.findNthDigit(12)