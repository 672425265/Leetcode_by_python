# coding: utf-8

'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j])
where the two words do not share common letters. You may assume
that each word will contain only lower case letters. If no such two words exist, return 0.
Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
'''

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if words is None or len(words) <= 1:
            return 0
        length = len(words)
        count = [len(item) for item in words]
        processWords = [0] * length

        for i in range(length):
            processWords[i] = 0
            for j in range(len(words[i])):
                processWords[i] |= (1 << ord(words[i][j]) - ord('a'))

        res = 0
        for i in range(length):
            for j in range(i+1, length):
                if processWords[i] & processWords[j] == 0:
                    res = max(res, count[i] * count[j])
        return res

solution = Solution()
print solution.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])