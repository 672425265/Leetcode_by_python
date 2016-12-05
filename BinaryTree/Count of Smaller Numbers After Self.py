# coding: utf-8

'''
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements
to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
'''

'''
思路是将给定数组从最后一个开始，用二分法插入到一个新的数组，
这样新数组就是有序的，
那么此时该数字在新数组中的坐标就是原数组中其右边所有较小数字的个数
'''

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        t, res = [], [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            left, right = 0, len(t)
            while left < right:
                mid = left + (right - left) / 2
                if t[mid] >= nums[i]:
                    right = mid
                else:
                    left = mid + 1
            res[i] = right
            t.insert(right, nums[i])
        return res

solution = Solution()
print solution.countSmaller([5,2,6,1])