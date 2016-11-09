# coding: utf-8
'''
Given an integer n, generate all structurally unique BST's
(binary search trees) that store values 1...n.
For example,
Given n = 3, your program should return all 5 unique BST's
shown below.
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generate(self, start, end):
        rst = []
        if start > end:
            return [None]
        for i in range(start, end+1):
            left = self.generate(start, i-1)
            right = self.generate(i+1, end)
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    rst.append(root)
        return rst

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.generate(1, n)

solution = Solution()
print solution.generateTrees(3)