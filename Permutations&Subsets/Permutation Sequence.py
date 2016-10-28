# coding: utf-8

'''
The set [1,2,3,…,n] contains a total of n!
unique permutations.
By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
'''

class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        mod = 1
        candidates = []
        for i in range(1, n+1):
            mod *= i
            candidates.append(i)
        k -= 1
        sb = ""
        for i in range(0, n):
            mod /= (n - i)
            # 得到当前应选数字的序数
            first = k / mod
            # 得到用于计算下一位的 k
            k = k % mod
            sb += str(candidates[first])
            candidates.pop(first)
        return sb

solution = Solution()
print solution.getPermutation(3, 3)