# coding: utf-8
'''
Given n non-negative integers representing
an elevation map where the width of each bar is 1,
 compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''
'''
1. 看两边
2. 选小柱子,向内灌水
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        start, end = 0, length - 1
        size = 0
        if start >= end:
            return size
        leftheight = height[start]
        rightheight = height[end]
        while start < end:
            if leftheight < rightheight:
                start += 1
                if leftheight > height[start]:
                    size += leftheight - height[start]
                else:
                    leftheight = height[start]
            else:
                end -= 1
                if rightheight > height[end]:
                    size += rightheight - height[end]
                else:
                    rightheight = height[end]
        return size

solution = Solution()
print solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])