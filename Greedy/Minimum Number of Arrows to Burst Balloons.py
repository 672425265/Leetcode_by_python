# coding: utf-8

'''
There are a number of spherical balloons spread in two-dimensional space.
For each balloon, provided input is the start and end coordinates of the horizontal diameter.
Since it's horizontal, y-coordinates don't matter and hence
the x-coordinates of start and end of the diameter suffice.
Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis.
A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend.
There is no limit to the number of arrows that can be shot.
An arrow once shot keeps travelling up infinitely.
The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6])
and another arrow at x = 11 (bursting the other two balloons).
'''

'''
贪心算法（Greedy Algorithm）
按照气球的起点排序
变量emin记录当前可以一箭命中的气球终点坐标的最小值，初始化为+∞
遍历排序后的气球起始点坐标s, e
若emin < s，说明当前气球无法用一支箭射中，则令最终结果ans + 1，令emin=+∞
更新emin = min(emin, e)
'''

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        emin = MAXINT = 0x7FFFFFFF
        for s, e in sorted(points):
            if emin < s:
                ans += 1
                emin = MAXINT
            emin = min(emin, e)
        return ans + bool(points)

a = [[10,16], [2,8], [1,6], [7,12]]
solution = Solution()
print solution.findMinArrowShots(a)