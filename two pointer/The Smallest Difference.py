# coding: utf-8

'''
Given two array of integers(the first array is array A,
the second array is array B), now we are going to
find a element in array A which is A[i],
and another element in array B which is B[j],
so that the difference between A[i]
and B[j] (|A[i] - B[j]|) is as small as possible,
return their smallest difference.
'''
import sys

class Solution:
    # @param A, B: Two lists of integer
    # @return: An integer
    def smallestDifference(self, A, B):
        # write your code here
        if A is None or len(A) == 0 or B is None or len(B) == 0:
            return 0

        A.sort()
        B.sort()
        ai, bi = 0, 0
        minValue = sys.maxint
        while ai < len(A) and bi < len(B):
            minValue = min(minValue, abs(A[ai] - B[bi]))
            if A[ai] < B[bi]:
                ai += 1
            else:
                bi += 1
        return minValue

solution = Solution()
A = [3,4,6,7]
B = [2,3,8,9]
print solution.smallestDifference(A, B)