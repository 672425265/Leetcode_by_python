# coding: utf-8
'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.
For example,
Given s = "Hello World",
return 5.
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        newS = s.strip().split(' ')
        return len(newS[-1])

solution = Solution()
print solution.lengthOfLastWord("b   a    ")
