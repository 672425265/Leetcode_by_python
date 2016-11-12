# coding: utf-8
'''
Given a binary tree, flatten it to a linked list in-place.
For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        dummy = TreeNode(None)
        stack = [root]
        while stack:
            top = stack.pop()
            if not top:
                continue
            stack.append(top.right)
            stack.append(top.left)
            dummy.right = top
            dummy.left = None
            dummy = top