# coding: utf-8

'''
Given two strings, find the longest common substring.
'''
class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        ans = 0
        for i in xrange(len(A)):
            for j in xrange(len(B)):
                l = 0
                while i + l < len(A) and j + l < len(B) \
                        and A[i + l] == B[j + l]:
                    l += 1
                if l > ans:
                    ans = l
        return ans

class Solution2:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        f = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
        for i in xrange(1, len(A) + 1):
            for j in xrange(1, len(B) + 1):
                if A[i-1] == B[j-1]:
                    f[i][j] = f[i-1][j-1] + 1
                else:
                    f[i][j] = 0
        maxvalue = 0
        for i in range(1, (len(A)+1)):
            for j in range(1, (len(B)+1)):
                maxvalue = max(maxvalue, f[i][j])

        return maxvalue

solution = Solution2()
print solution.longestCommonSubstring("abcd","eacb")

'''
1. 状态
2.
'''