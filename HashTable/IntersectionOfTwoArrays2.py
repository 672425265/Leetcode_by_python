# -*- coding: utf-8 -*-

'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
1. Each element in the result must be unique.
2. The result can be in any order.
'''

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        result = []
        flag = set()
        while nums1 and nums2:
            if nums2[0] == nums1[0] and nums1[0] not in flag:
                result.append(nums2.pop(0))
                flag.add(nums1.pop(0))
            else:
                if nums2[0] > nums1[0]:
                    nums1.pop(0)
                else:
                    nums2.pop(0)
        return result


'''
Test:
nums1 = [1,2,2,1]
nums2 = [2,2]
'''

solution = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
res = solution.intersect(nums1, nums2)
print res