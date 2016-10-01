# coding: utf-8

'''
Given two words word1 and word2,
find the minimum number of steps required
to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # distance[i][j]代表word1的前i个字符,
        # 匹配上word2的前j个字符的最小转换次数
        if word1 is None or word2 is None:
            return None

        distance = [[0] * (len(word2) + 1)
                    for i in range(len(word1) + 1)]

        for i in xrange(0, len(word1) + 1):
            distance[i][0] = i

        for j in xrange(0, len(word2) + 1):
            distance[0][j] = j

        for i in xrange(1, len(word1) + 1):
            for j in xrange(1, len(word2) + 1):
                distance[i][j] = min(distance[i-1][j], distance[i][j-1]) + 1
                if word1[i-1] == word2[j-1]:
                    distance[i][j] = min(distance[i][j],
                                     distance[i-1][j-1])
                else:
                    distance[i][j] = min(distance[i][j],
                                         distance[i - 1][j - 1] + 1)


        return distance[len(word1)][len(word2)]

solution = Solution()
print solution.minDistance("b", "")