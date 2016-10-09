# coding: utf-8
'''
Follow up for H-Index: What if the citations array
is sorted in ascending order? Could you optimize your algorithm?
'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n == 0:
            return 0
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) / 2
            if citations[mid] < n - mid:
                start = mid + 1
            else:
                end = mid - 1

        return n - start


class Solution2(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        low, high = 0, N - 1
        while low <= high:
            mid = (low + high) / 2
            if N - mid > citations[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return N - low

solution = Solution()
print solution.hIndex([0,0,0])