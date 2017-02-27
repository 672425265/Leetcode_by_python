# coding: utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        list = []
        list.append(root)
        while len(list) > 0:
            next = []
            size = len(list)
            for i in range(0, size):
                cur = list.pop(0)
                if i == 0:
                    res = cur.val
                if cur.left is not None:
                    next.append(cur.left)
                if cur.right is not None:
                    next.append(cur.right)
            list = next
        return res