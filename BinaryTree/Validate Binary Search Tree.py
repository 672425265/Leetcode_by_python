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

class ResultType(object):
    def __init__(self, is_bst, maxValue, minValue):
        self.is_bst = is_bst
        self.maxValue = maxValue
        self.minValue = minValue

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = self.validate(root)
        return result.is_bst

    def validate(self, root):
        if root is None:
            return ResultType(True, -sys.maxint - 1, sys.maxint)
        left = self.validate(root.left)
        right = self.validate(root.right)

        if left.is_bst == False or right.is_bst == False:
            return ResultType(False, 0, 0)

        if (root.left is not None and left.maxValue >= root.val) \
                or (root.right is not None and right.minValue <= root.val):
            return ResultType(False, 0, 0)

        return ResultType(True, max(root.val, right.maxValue)
                          , min(root.val, left.minValue))

class Solution2:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        self.lastVal = None
        self.isBST = True
        self.validate(root)
        return self.isBST

    def validate(self, root):
        if root is None:
            return
        self.validate(root.left)
        if self.lastVal is not None and self.lastVal >= root.val:
            self.isBST = False
            return
        self.lastVal = root.val
        self.validate(root.right)


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

solution = Solution()
result = solution.isValidBST(root)
print result
