# coding: utf-8
'''
Given a binary tree, determine if it is a valid
binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with
keys less than the node's key.
The right subtree of a node contains only nodes with
keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

import sys
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.dfs(root, -1 * sys.maxint, sys.maxint)

    def dfs(self, root, low, up):
        if root is None:
            return True
        if root.val >= up or root.val <= low:
            return False
        return self.dfs(root.left, low, root.val) and self.dfs(root.right, root.val, up)


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

solution = Solution()
result = solution.isValidBST(root)
print result
