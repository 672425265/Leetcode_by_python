# coding: utf-8

'''
Find the length of the longest substring T of a given string (consists of lowercase letters only)
such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''

'''
递归（Recursion）/ 分治法（Divide and Conquer）

统计原始字符串s中各字符的出现次数，统计其中出现次数少于k次的字符，得到数组filters。

若filters为空数组，则直接返回s的长度。

以filters为分隔符，将s拆分为若干子串，分别递归计算各子串的结果，返回最大值。
'''
from collections import Counter
import re

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = Counter(s)
        filters = [x for x in cnt if cnt[x] < k]
        if not filters:
            return len(s)
        tokens = re.split('|'.join(filters), s)
        return max(self.longestSubstring(t, k) for t in tokens)

solution = Solution()
s = "ababbcd"
k = 2
print solution.longestSubstring(s, k)