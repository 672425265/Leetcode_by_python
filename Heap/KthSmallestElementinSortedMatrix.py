'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.
'''
import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        arr = []
        for item in matrix:
            for son in item:
                arr.append(son)
        arr = sorted(arr)
        return arr[k-1]

class Solution2(object):
    def kthSmallest(self, matrix, k):
        result, heap = None, []
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        while k > 0:
            result, i, j = heapq.heappop(heap)
            if i == 0 and j + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
            if i + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i+1][j], i+1, j))
            k -= 1
        return result

solution = Solution2()
k = solution.kthSmallest([[1,2],[1,3]],2)
print k