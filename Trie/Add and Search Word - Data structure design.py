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
        self.leaf = False
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def insert(self, s):
        if len(s) == 0:
            return
        p = self.root
        i = 0
        while i < len(s):
            if p.children[ord(s[i]) - ord('a')] is None:
                new_node = TrieNode()
                p.children[ord(s[i]) - ord('a')] = new_node
            p = p.children[ord(s[i]) - ord('a')]
            i += 1
        p.leaf = True
        self.size += 1

    def search(self, s):
        if len(s) == 0:
            return False

        return self.searchRe(s, self.root, 0)

    def searchRe(self, s, p, i):
        if len(s) == i:
            if p.leaf:
                return True
            return False

        result = False
        if s[i] == '.':
            for j in range(0, 26):
                if p.children[j] != None:
                    if self.searchRe(s, p.children[j], i + 1):
                        result = True
        else:
            if p.children[ord(s[i]) - ord('a')] != None:
                if self.searchRe(s, p.children[ord(s[i]) - ord('a')], i + 1):
                    result = True
        return result

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.trie = Trie()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.trie.insert(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")