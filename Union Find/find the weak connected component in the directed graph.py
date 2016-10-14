# coding: utf-8

'''
Find the number Weak Connected Component in the directed graph.
Each node in the graph contains a label
and a list of its neighbors.
(a connected set of a directed graph is a subgraph in which
	any two vertices are connected by direct edge path.)
Example
Given graph:
A----->B  C
 \     |  |
  \    |  |
   \   |  |
    \  v  v
     ->D  E <- F
Return {A,B,D}, {C,E,F}. Since there are
two connected component which are {A,B,D} and {C,E,F}
Note
Sort the element in the set in increasing order
Tags Expand
Union Find
'''
import collections

# Definition for a directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class UnionFind:
    def __init__(self, labels):
        self.father = {}
        for x in labels:
            self.father[x] = x

    def compressed_find(self, x):
        parent = self.father.get(x)
        while parent != self.father.get(parent):
            parent = self.father.get(parent)

        # compressed path
        temp = -1
        fa = self.father.get(x)
        while fa != self.father.get(fa):
            temp = self.father.get(fa)
            self.father[fa] = parent
            fa = temp

        return parent

    def union(self, x, y):
        fa_x = self.compressed_find(x)
        fa_y = self.compressed_find(y)

        if fa_x != fa_y:
            self.father[fa_x] = fa_y


class Solution:
    # @param {DirectedGraphNode[]} nodes a array of directed graph node
    # @return {int[][]} a connected set of a directed graph
    def connectedSet2(self, nodes):
        # Write your code here
        labels = set()

        # traversal lebals
        for node in nodes:
            labels.add(node.label)
            for n in node.neighbors:
                labels.add(n.label)

        uf = UnionFind(labels)

        # union
        for node in nodes:
            for n in node.neighbors:
                fa_node = uf.compressed_find(node.label)
                fa_neigh = uf.compressed_find(n.label)
                if fa_node != fa_neigh:
                    uf.union(node.label, n.label)

        return self.helper(labels, uf)

    def helper(self, labels, uf):
        ans = []
        neighDict = collections.defaultdict(list)

        for l in labels:
            fa = uf.compressed_find(l)
            neighDict[fa].append(l)

        for v in neighDict.values():
            v.sort()
            ans.append(v)

        return ans

a = DirectedGraphNode("A")
b = DirectedGraphNode("B")
c = DirectedGraphNode("C")
d = DirectedGraphNode("D")
f = DirectedGraphNode("F")
e = DirectedGraphNode("E")
a.neighbors = [b, d]
b.neighbors = [d]
c.neighbors = [e]
f.neighbors = [e]
solution = Solution()
print solution.connectedSet2([a, b, c, d, e, f])