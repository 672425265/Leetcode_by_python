# coding: utf-8

'''
Given a binary tree, return the preorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return preorder


class Solution2(object):
    def traverse(self, root, result):
        if root is None:
            return []
        result.append(root.val)
        self.traverse(root.left, result)
        self.traverse(root.right, result)

    def preorderTraversal(self, root):
        result = []
        self.traverse(root, result)
        return result
