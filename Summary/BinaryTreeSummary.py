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

    def maxDepthRec(self, root):
        if root is None:
            return 0
        left = self.maxDepthRec(root.left)
        right = self.maxDepthRec(root.right)
        return max(left, right) + 1

    def maxDepth(self, root):
        if root is None:
            return 0
        depth = 0
        currentLevelNodes = 1
        nextLevelNodes = 0
        queue = []
        queue.append(root)
        while len(queue) > 0:
            cur = queue.pop()
            currentLevelNodes -= 1
            if cur.left is not None:
                queue.append(cur.left)
                nextLevelNodes += 1
            if cur.right is not None:
                queue.append(cur.right)
                nextLevelNodes += 1
            if currentLevelNodes == 0:
                depth += 1
                currentLevelNodes = nextLevelNodes
                nextLevelNodes = 0
        return depth

a = Solution()
# print a.getNodeSum(root)
print a.maxDepthRec(root)
print a.maxDepth(root)
