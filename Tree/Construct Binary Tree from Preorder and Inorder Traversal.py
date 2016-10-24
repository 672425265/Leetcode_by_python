# coding: utf-8

'''
Given preorder and inorder traversal of a tree, construct the binary tree.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        rootPos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+rootPos], inorder[:rootPos])
        root.right = self.buildTree(preorder[rootPos+1:], inorder[rootPos+1:])
        return root

class Solution2(object):
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        self.preorder, self.inorder = preorder, inorder
        return self.dfs(0, len(preorder) - 1, 0, len(inorder) - 1)

    def dfs(self, L1, R1, L2, R2):
        if L1 > R1:
            return None
        if L1 == R1:
            return TreeNode(self.preorder[L1])
        root = TreeNode(self.preorder[L1])
        # rootPos is the index of current root (preorder[L1]) in inorder list
        rootPos = self.inorder.index(self.preorder[L1])
        root.left = self.dfs(L1 + 1, L1 + rootPos - L2, L2, rootPos - 1)
        root.right = self.dfs(L1 + rootPos - L2 + 1, R1, rootPos + 1, R2)
        return root