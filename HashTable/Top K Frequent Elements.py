# coding: utf-8
'''
Given a non-empty array of integers, return the k most frequent elements.
For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = dict()
        ans = []
        for i in nums:
            count[i] = count.get(i, 0) + 1
        count = sorted(count.iteritems(), key=lambda d: d[1], reverse=True)
        start = 0
        while start < k:
            ans.append(count[start][0])
            start += 1
        return ans

solution = Solution()
print solution.topKFrequent([1,1,1,2,2,3], 2)