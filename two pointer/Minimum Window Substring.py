# coding: utf-8
'''
Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).
For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".
Note:
If there is no such window in S that covers all characters in T,
return the empty string "".
If there are multiple such windows, you are guaranteed that
there will always be only one unique minimum window in S.
'''

class Solution:
    # @return a string
    def minWindow(self, S, T):
        m, n = len(S), len(T)
        dic, cnt = [0] * 129, [0] * 129
        for i in T:
            cnt[ord(i)] += 1
            dic[ord(i)] += 1

        start, L, dis = 0, 0, m + 1
        for i in range(m):
            if dic[ord(S[i])] > 0:
                cnt[ord(S[i])] -= 1
                if cnt[ord(S[i])] >= 0:
                    n -= 1
            if n == 0:
                while start <= i:
                    if dic[ord(S[start])] > 0:
                        if cnt[ord(S[start])] < 0:
                            cnt[ord(S[start])] += 1
                        else:
                            break
                    start += 1
                if i - start + 1 < dis:
                    dis = i - start + 1
                    L = start
        if dis != m + 1:
            return S[L:L + dis]
        return ""

solution = Solution()
S = "ADOBECODEBANC"
T = "ABCC"
print solution.minWindow(S, T)

