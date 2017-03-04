#coding: utf-8

'''
Given a string s and a dictionary of words dict,
determine if s can be segmented into a space-separated
sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if len(dict) == 0:
            return len(s) == 0

        n = len(s)
        cansegment = [False] * (n+1)
        cansegment[0] = maxlength = max([len(w) for w in wordDict])
        for i in xrange(1, n+1):
            lastwordlength = 1
            while lastwordlength <= maxlength and lastwordlength <= i:
                # 判断前面 i- lastwordlength 个词可不可以分
                if not cansegment[i - lastwordlength]:
                    lastwordlength += 1
                    continue
                word = s[i-lastwordlength:i]
                if word in wordDict:
                    cansegment[i] = True
                    break
                lastwordlength += 1
        return cansegment[n]


class Solution2(object):
    def wordBreak(self, s, dict):
        if len(dict) == 0:
            return len(s) == 0

        n = len(s)
        f = [False] * (n + 1)
        f[0] = True

        maxLength = max([len(w) for w in dict])
        for i in xrange(1, n + 1):
            for j in range(1, min(i, maxLength) + 1):
                # 判断前 i-j 个词可不可以分
                if not f[i - j]:
                    continue
                # 如果可以分, 则再看后 i-j 个词
                if s[i - j:i] in dict:
                    f[i] = True
                    break
        return f[n]


s = "leetcode"
dict = ["leet", "code", "leetc", "ode"]
solution = Solution()
print solution.wordBreak(s,dict)