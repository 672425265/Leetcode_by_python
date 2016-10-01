# coding: utf-8

'''
Given s1, s2, s3, find whether s3 is formed
by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if s1 is None or s2 is None or s3 is None:
            return False
        if len(s1) + len(s2) != len(s3):
            return False

        interleave = [[False] * (len(s2) + 1)
                      for i in range(len(s1) + 1)]

        interleave[0][0] = True
    # interleave[i][j] 代表s1的前i个字符,和s2的前j个字符,能否匹配s3的前i+j个字符
        for i in range(1, len(s1) + 1):
          interleave[i][0] = s1[:i] == s3[:i]
        for i in range(1, len(s2) + 1):
            interleave[0][i] = s2[:i] == s3[:i]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                # 如果s1的第i个字符和s3的最后一个相等,那么就按s1的最后一个字符匹配
                if s1[i-1] == s3[i+j-1]:
                    interleave[i][j] = interleave[i][j] or interleave[i-1][j]
                if s2[j-1] == s3[i+j-1]:
                    interleave[i][j] = interleave[i][j] or interleave[i][j-1]

        return interleave[len(s1)][len(s2)]

solution = Solution()
s1 = "ab"
s2 = "bc"
s3 = "babc"
s4 = "aadbbbaccc"

print solution.isInterleave(s1, s2, s3)