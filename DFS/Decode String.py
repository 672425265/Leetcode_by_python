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

'''
利用栈（Stack）数据结构。

当出现左括号时，将字符串压栈。

当出现右括号时，将字符串弹栈，并重复响应次数，累加至新的栈顶元素。
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
                cur += tmp * intStack.pop()
            else:
                cur += c
        return cur

solution = Solution()
s = "3[a]2[bc]"
print solution.decodeString(s)