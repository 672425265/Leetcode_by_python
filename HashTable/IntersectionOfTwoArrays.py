# -*- coding: utf-8 -*-

'''

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
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
        while nums1 and nums2:
            if nums2[0] == nums1[0]:
                result.append(nums2.pop(0))
                nums1.pop(0)
            else:
                if nums2[0] > nums1[0]:
                    nums1.pop(0)
                else:
                    nums2.pop(0)
        return result

'''
方法二

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count = {}
        res = []
        for item in nums1:
            if item not in count:
                count[item] = [1, 0]
            else:
                count[item][0] += 1
        for item in nums2:
            if item in count:
                count[item][1] +=1

        for key in count:
            if count[key][0] * count[key][1] > 0:
                for i in range(min(count[key][0], count[key][1])):
                    res.append(key)

        return res
'''



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