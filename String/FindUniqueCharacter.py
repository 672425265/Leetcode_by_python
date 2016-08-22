# -*- coding: utf-8 -*-

'''
Given a string, find the first non-repeating character
in it and return it's index. If it doesn't exist, return -1.

Example:
    s = "leetcode"
    return 0.

    s = "loveleetcode",
    return 2.
'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for x in s:
            if s.find(x) == s.rfind(x):
                return s.find(x)
        return -1

'''
Test:
s = 'leetcode'

'''
s = 'loveleetcode'
solution = Solution()
index = solution.firstUniqChar(s)
print index

