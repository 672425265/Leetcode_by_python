# coding: utf-8

'''
Given a binary search tree, write a function
kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations)
often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?

Show Hint
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        s = []
        while root is not None:
            s.append(root)
            root = root.left
        while len(s) > 0:
            cur = s.pop()
            k -= 1
            if k == 0:
                return cur.val
            if cur.right is not None:
                cur = cur.right
                while cur is not None:
                    s.append(cur)
                    cur = cur.left
        return 0
