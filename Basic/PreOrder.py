# coding: utf-8
class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in list which contains node values.
    """
    # version1
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder

    # version2 Traverse
    def preorderinit(self, root):
        result = []
        self.preorderTraversal2(root, result)
        return result
    result = []
    def preorderTraversal2(self, root, result):
        if root == None:
            return
        result.append(root.val)
        self.preorderTraversal2(root.left, result)
        self.preorderTraversal2(root.right, result)


    # version3 Divide & Conquer
    def preorderTraversal3(self, root):
        result = []
        if root == None:
            return result

        left = self.preorderTraversal3(root.left)
        right = self.preorderTraversal3(root.right)

        result.append(root.val)
        for item in left:
            result.append(item)
        for item in right:
            result.append(item)
        return result

root = TreeNode(1)
left = TreeNode(3)
right = TreeNode(3)
root.left = left
root.right = right

solution = Solution()
a = solution.preorderTraversal3(root)
print a