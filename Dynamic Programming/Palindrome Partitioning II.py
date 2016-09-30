# coding: utf-8

'''
Given a string s, partition s such that every substring
of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"]
could be produced using 1 cut.
'''


class Solution(object):
    def getisPalindrome(self, s):
        isPalindrome = [[False] * len(s) for i in range(len(s))]

        for i in xrange(0, len(s)):
            isPalindrome[i][i] = True

        for i in xrange(0, len(s) - 1):
            isPalindrome[i][i + 1] = (s[i] == s[i+1])

        for length in xrange(2, len(s)):
            # 区间动态规划,先枚举区间长度,再枚举区间起点
            start = 0
            while start + length < len(s):
                isPalindrome[start][start + length] = \
                    isPalindrome[start+1][start+length-1] \
                    and s[start] == s[start + length]
                start += 1

        return isPalindrome

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0

        isPalindrome = self.getisPalindrome(s)

        f = [0] * (len(s) + 1)
        f[0] = 0

        for i in xrange(1, len(s) + 1):
            f[i] = i
            for j in xrange(0, i):
                # 如果说从 j+1 到 i 是一个回文串
                if isPalindrome[j][i - 1]:
                    # f[i]是前i个字母,最少可被分为回文串的个数
                    f[i] = min(f[i], f[j] + 1)

        return f[len(s)] - 1

solution = Solution()
print solution.minCut("aaa")