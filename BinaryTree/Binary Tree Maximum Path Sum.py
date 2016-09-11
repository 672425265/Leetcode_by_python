# coding: utf-8
'''
Given a binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes
from some starting node to any node in the tree along the
parent-child connections. The path does not need
to go through the root.
For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# version1:
# singlePath: 从root往下走到任意点的最大路径，这条路径可以不包含任何点
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxSum, _ = self.maxPathHelper(root)
        return maxSum

    def maxPathHelper(self, root):
        if root is None:
            return  None, 0
        left = self.maxPathHelper(root.left)
        right = self.maxPathHelper(root.right)
        maxpath = max(left[0], right[0],
                      root.val + left[1] + right[1])
        single = max(left[1] + root.val, right[1] + root.val, 0)
        return maxpath, single

# Version 2:
# SinglePath也定义为，至少包含一个点。
class Solution2(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxSum, _ = self.maxPathHelper(root)
        return maxSum

    def maxPathHelper(self, root):
        if root is None:
            return  None, 0
        left = self.maxPathHelper(root.left)
        right = self.maxPathHelper(root.right)
        single = max(left[1], right[1], 0) + root.val
        maxpath = max(left[0], right[0],
                      root.val + left[1] + right[1])
        return maxpath, single