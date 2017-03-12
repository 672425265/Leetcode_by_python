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
    # non traverse
    def postorderTraversal(self, root):
        if root is None:
            return []
        stack = []
        res = []
        pre = None
        stack.append(root)
        '''
        要保证左孩子和右孩子都已被访问并且左孩子在右孩子前访问才能访问根结点
        '''
        while stack:
            cur = stack[-1]
            if (cur.left is None and cur.right is None) or \
                (pre is not None and (pre == cur.left or pre == cur.right)):
                res.append(cur.val)
                stack.pop()
                pre = cur
            else:
                if cur.right is not None:
                    stack.append(cur.right)
                if cur.left is not None:
                    stack.append(cur.left)

        return res


    # version2 Traverse
    def preorderinit(self, root):
        result = []
        self.preorderTraversal2(root, result)
        return result

    def preorderTraversal2(self, root, result):
        if root is None:
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