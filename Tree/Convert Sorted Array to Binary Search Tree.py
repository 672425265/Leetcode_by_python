# coding: utf-8
'''
Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, nums, start, end):
        if start > end:
            return None
        node = TreeNode(nums[(start + end) / 2])
        node.left = self.buildTree(nums, start, (start + end) / 2 - 1)
        node.right = self.buildTree(nums, (start + end) / 2 + 1, end)
        return node

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums is None:
            return None
        return self.buildTree(nums, 0, len(nums) - 1)