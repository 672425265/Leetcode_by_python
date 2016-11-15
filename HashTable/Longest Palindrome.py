# coding: utf-8
'''
Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
Note:
Assume the length of given string will not exceed 1,010.
Example:
Input:
"abccccdd"
Output:
7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)
        res = 0
        flag = False
        for key in count:
            if count[key] % 2 == 0:
                res += count[key]
            if count[key] % 2 == 1:
                res += count[key] - 1
                flag = True
        if flag:
            return res + 1
        else:
            return res

solution = Solution()
print solution.longestPalindrome("ccc")