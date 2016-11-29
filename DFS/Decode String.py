# coding: utf-8

'''
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string
inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces,
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k. For example,
there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        k = 0
        intStack = []
        strStack = []
        cur = ""
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == '[':
                intStack.append(k)
                strStack.append(cur)
                cur = ""
                k = 0
            elif c == ']':
                tmp = cur
                cur = strStack.pop()
                for i in range(intStack.pop(), 0, -1):
                    cur += tmp
            else:
                cur += c
        return cur

solution = Solution()
s = "3[a]2[bc]"
print solution.decodeString(s)