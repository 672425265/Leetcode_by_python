# coding: utf-8

'''
Find the sum of all left
leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree,
with values 9 and 15 respectively. Return 24.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def search(self, root, now):
        if root.left is None and root.right is None:
            if now == 1:
                return root.val
            else:
                return 0
        sum = 0
        if root.left is not None:
            sum += self.search(root.left, 1)
        if root.right is not None:
            sum += self.search(root.right, 0)
        return sum

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is not None:
            return self.search(root, 0)
        return 0

class Solution2(object):
    def dfs(self, root, isLeft):
        if root is None:
            return 0
        if root.left is None and root.right is None and isLeft:
            return root.val
        return self.dfs(root.left, True) + self.dfs(root.right, False)

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, False)