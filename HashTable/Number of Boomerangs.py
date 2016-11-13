# coding: utf-8
'''
Given n points in the plane that are all pairwise distinct,
a "boomerang" is a tuple of points (i, j, k) such that
the distance between i and j
equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n
will be at most 500 and coordinates of points are all
in the range [-10000, 10000] (inclusive).
Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2
Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]]
and [[1,0],[2,0],[0,0]]
'''

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(0, len(points)):
            m = dict()
            for j in range(0, len(points)):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                m[x**2 + y**2] = m.get(x**2 + y**2, 0) + 1
            for item in m:
                res += m[item] * (m[item] - 1)
        return res

solution = Solution()
print solution.numberOfBoomerangs([[0,0],[1,0],[2,0]])
