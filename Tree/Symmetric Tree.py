#coding: utf-8
'''
Given a binary tree, check whether
it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric_2(self, left, right):
        if not left and not right:
            return True
        if (not left and right) or (not right and left) \
                or left.val != right.val:
            return False
        return self.isSymmetric_2(left.left, right.right) \
               and self.isSymmetric_2(left.right, right.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSymmetric_2(root.left, root.right)


class Solution2(object):
    def isSymmetric_2(self, left, right):
        if not left and not right:
            return True
        if (not left and right) or (not right and left):
            return False
        s1 = []
        s2 = []
        s1.append(left)
        s2.append(right)
        while len(s1) and len(s2):
            cur1 = s1.pop()
            cur2 = s2.pop()

            if cur1.val != cur2.val:
                return False

            if cur1.left is not None and cur2.right is not None:
                s1.append(cur1.left)
                s2.append(cur2.right)
            elif not (cur1.left is None and cur2.right is None):
                return False

            if cur1.right is not None and cur2.left is not None:
                s1.append(cur1.right)
                s2.append(cur2.left)
            elif not (cur1.right is None and cur2.left is None):
                return False

        return True

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSymmetric_2(root.left, root.right)