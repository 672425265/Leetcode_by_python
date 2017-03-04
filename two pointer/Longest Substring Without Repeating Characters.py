# coding: utf-8

'''
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
'''

class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = dict()
        j = 0
        ans = 0
        stack = []
        for i in range(0, len(s)):
            while j < len(s) and not map.has_key(s[j]):
                map[s[j]] = map.get(s[j], 1)
                ans = max(ans, j-i+1)
                j += 1
            map.pop(s[i])

        return ans

solution = Solution()
print solution.lengthOfLongestSubstring("pwwkew")


