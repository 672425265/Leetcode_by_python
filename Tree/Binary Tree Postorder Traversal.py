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
return [3,2,1].
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        postorder = []
        while stack:
            node = stack.pop()
            postorder.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        postorder = list(reversed(postorder))
        return postorder


class Solution2(object):
    def traverse(self, root, result):
        if root is None:
            return []
        self.traverse(root.left, result)
        self.traverse(root.right, result)
        result.append(root.val)

    def postorderTraversal(self, root):
        result = []
        self.traverse(root, result)
        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print Solution2().postorderTraversal(root)
