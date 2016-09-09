# coding: utf-8
'''
Given an input string, reverse the string word by word.
For example,
Given s = "the sky is blue",
return "blue is sky the".
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(reversed(s.split()))

solution = Solution()
s = "the sky is blue"
solution.reverseWords(s)
print s