# coding: utf-8

'''
Given n nodes labeled from 0 to n - 1 and
a list of undirected edges (each edge is a pair of nodes),
write a function to find the number of connected components
in an undirected graph.

Example 1:

    0          3
    |          |
    1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:

    0           4
    |           |
    1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.
'''

class Solution(object):
    def countComponents(self, n, edges):
        father = [0] * n

        # 初始化
        for node in xrange(n):
            father[node] = node

        # union
        for edge in edges:
            i = self.find(father, edge[0])
            j = self.find(father, edge[1])
            father[i] = j

        # 统计根节点个数
        count = 0
        for i in xrange(n):
            if father[i] == i:
                count += 1
        return count

    def find(self, father, node):
        while node != father[node]:
            father[node] = father[father[node]]
            node = father[node]
        return node


solution = Solution()
print solution.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]])
