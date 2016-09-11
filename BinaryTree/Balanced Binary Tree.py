# coding: utf-8
'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined
as a binary tree in which the depth of the
two subtrees of every node never differ by more than 1.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        balanced, _ = self.validate(root)

    def validate(self, root):
        if root is None:
            return True, 0

        balanced, leftHeight = self.validate(root.left)
        if not balanced:
            return False, 0
        balanced, rightHeight = self.validate(root.right)
        if not balanced:
            return False, 0

        return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight)

    class Solution2(object):
        def isBalanced(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            return self.maxDepth(root) != -1

        def maxDepth(self, root):
            if root is None:
                return 0
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1
