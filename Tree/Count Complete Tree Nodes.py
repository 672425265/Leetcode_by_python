# coding: utf-8
'''
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible.

It can have between 1 and 2h nodes inclusive at the last level h.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def leftHeight(root):
            if not root:
                return 0
            return 1 + leftHeight(root.left)

        def rightHeight(root):
            if not root:
                return 0
            return 1 + rightHeight(root.right)

        hLeft = leftHeight(root)
        hRight = rightHeight(root)
        if hLeft == hRight:
            return (1 << hLeft) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1