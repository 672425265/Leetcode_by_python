# coding: utf-8

'''
Given inorder and postorder traversal of a tree, construct the binary tree.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        rootPos = inorder.index(postorder[-1])
        postorder.pop()
        root.left = self.buildTree(inorder[:rootPos], postorder)
        root.right = self.buildTree(inorder[rootPos+1:], postorder)
        return root

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        self.inorder, self.postorder = inorder, postorder
        return self.dfs(0, 0, len(inorder))

    def dfs(self, inLeft, postLeft, len):
        if len <= 0:
            return None
        root = TreeNode(self.postorder[postLeft + len - 1])
        rootPos = self.inorder.index(self.postorder[postLeft + len - 1])
        root.left = self.dfs(inLeft, postLeft, rootPos - inLeft)
        root.right = self.dfs(rootPos + 1, postLeft + rootPos - inLeft, len - 1 - (rootPos - inLeft))
        return root

solution = Solution()
print solution.buildTree()