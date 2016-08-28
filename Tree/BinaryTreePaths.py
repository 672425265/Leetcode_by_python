# coding: utf-8
'''
Given a binary tree, return all root-to-leaf paths.
For example, given the following binary tree:
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        elif not root.left and not root.right:
            return [str(root.val)]
        else:
            return list(map(lambda x: str(root.val) + "->" + x, self.binaryTreePaths(root.left)
                            + self.binaryTreePaths(root.right)))

    def binaryTreePaths2(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]

        leftPathToLeaf = self.binaryTreePaths2(root.left)
        rightPathToleaf = self.binaryTreePaths2(root.right)

        left = [str(root.val) + ("->" + lpath) for lpath in leftPathToLeaf]
        right = [str(root.val) + ("->" + rpath) for rpath in rightPathToleaf]

        return left + right
