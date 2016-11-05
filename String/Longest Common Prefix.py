# coding: utf-8
'''
Write a function to find the longest common prefix
string amongst an array of strings.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < len(strs[i]) and j < len(prefix) and strs[i][j] == prefix[j]:
                j += 1
            if j == 0:
                return ""
            prefix = prefix[0:j]
        return prefix

solution = Solution()
print solution.longestCommonPrefix(["psa","psb","psc"])