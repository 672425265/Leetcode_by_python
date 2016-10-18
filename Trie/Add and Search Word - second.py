# coding: utf-8
'''
Design a data structure that supports
the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a
regular expression string containing
only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
'''


class TrieNode:
    def __init__(self):
        self.hasWord = False
        self.children = [None] * 26


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        now = self.root
        for i in range(0, len(word)):
            c = word[i]
            if now.children[ord(c) - ord('a')] is None:
                now.children[ord(c) - ord('a')] = TrieNode()
            now = now.children[ord(c) - ord('a')]
        now.hasWord = True

    def find(self, word, index, now):
        if index == len(word):
            return now.hasWord

        c = word[index]
        if c == '.':
            for i in range(0, 26):
                if now.children[i] is not None:
                    if self.find(word, index + 1, now.children[i]):
                        return True
            return False
        elif now.children[ord(c) - ord('a')] is not None:
            return self.find(word, index + 1, now.children[ord(c) - ord('a')])
        else:
            return False

    def search(self, word):
        return self.find(word, 0, self.root)

