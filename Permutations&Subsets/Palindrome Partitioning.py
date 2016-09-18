#coding: utf-8

'''
Given a string s, partition s such that every substring
of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
'''

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        if s is None or len(s) == 0:
            return result
        path = []
        self.helper(s, path, 0, result)

        return result

    def isPalindrome(self, s):
        beg = 0
        end = len(s) - 1
        while beg < end:
            if s[beg] != s[end]:
                return False
            beg += 1
            end -= 1
        return True

    def helper(self, s, path, pos, result):
        if pos == len(s):
            result.append([] + path)
            return
        for i in xrange(pos, len(s)):
            prefix = s[pos:i+1]
            if not self.isPalindrome(prefix):
                continue
            path.append(prefix)
            self.helper(s, path, i + 1, result)
            path.pop()

solution = Solution()
print solution.partition("aab")