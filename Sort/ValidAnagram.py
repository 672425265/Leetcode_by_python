# coding: utf-8
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = []
        b = []
        for i in s:
            a.append(i)
        for j in t:
            b.append(j)

        a.sort()
        b.sort()
        if a.__eq__(b):
            return True
        else:
            return False

    def isAngram2(self, s, t):
        if set(s) != set(t):
            return False
        else:
            for element in set(s):
                if s.count(element) != t.count(element):
                    return False
            return True

solution = Solution()
s = "anagram"
t = "nagaram"
c = solution.isAngram2(s, t)
print c