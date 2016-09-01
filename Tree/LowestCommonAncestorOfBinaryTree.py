# coding: utf-8
'''
Given a binary tree, find the lowest common ancestor
(LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor
is defined between two nodes v and w as the lowest node in T that
has both v and w as descendants (where we allow a node to be a descendant of itself).”
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if not root or root == p or root == q:
                return root
            if self.isnode(p, q):
                return p
            if self.isnode(q, p):
                return q
            if self.isnode(root.left, p) and self.isnode(root.left, q):
                root = root.left
            if self.isnode(root.right, p) and self.isnode(root.right, q):
                root = root.right
            else:
                return root



    def isnode(self, mother, child):
        if mother:
            if mother == child:
                return True
            else:
                return self.isnode(mother.left, child) or \
                       self.isnode(mother.right, child)
        return False