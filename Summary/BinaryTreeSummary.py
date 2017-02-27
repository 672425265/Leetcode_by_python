# coding: utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = None
        self.left = None
        self.right = None

root = TreeNode(5)
n1 = TreeNode(4)
n2 = TreeNode(3)
n3 = TreeNode(2)
n4 = TreeNode(1)
n5 = TreeNode(6)
root.left = n1
n1.left = n2
n2.left = n3
n3.left = n4
root.right = n5

class Solution(object):
    def getNodeSum(self, root):
        if root is None:
            return 0
        else:
            return self.getNodeSum(root.left) + self.getNodeSum(root.right) + 1
    def maxDepth(self, root):
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


a = Solution()
print a.getNodeSum(root)
print a.maxDepth(root)
