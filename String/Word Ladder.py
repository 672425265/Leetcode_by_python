# coding: utf-8
'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
'''
import collections

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.add(endWord)
        wordLen = len(beginWord)
        queue = collections.deque([(beginWord, 1)])
        while queue:
            curr = queue.popleft()
            currWord = curr[0]
            currLen = curr[1]
            if currWord == endWord: return currLen
            for i in xrange(wordLen):
                part1 = currWord[:i]
                part2 = currWord[i + 1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currWord[i] != j:
                        nextWord = part1 + j + part2
                        if nextWord in wordList:
                            queue.append((nextWord, currLen + 1))
                            wordList.remove(nextWord)
        return 0

solution = Solution()
print solution.ladderLength("hit", "cog", set(["hot","dot","dog","lot","log"]))