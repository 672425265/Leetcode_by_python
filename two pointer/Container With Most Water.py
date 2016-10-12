# coding: utf-8

'''
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines,
which together with x-axis forms a container,
such that the container contains the most water.

Note: You may not slant the container.

example:
给出[1,3,2], 最大的储水面积是2.
'''


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        maxValue = None
        while left <= right:
            area = (right - left) * min(height[right], height[left])
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            maxValue = max(maxValue, area)
        return maxValue

solution = Solution()
print solution.maxArea([1,3,2])


