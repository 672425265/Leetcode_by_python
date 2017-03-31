# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        res = []
        path = []
        self.dfs(root, res, path, sum)
        return len(res) is not None

    def dfs(self, root, res, path, sum):
        if root is None:
            return
        sum -= root.val
        if root.left is None or root.right is None:
            if sum == 0:
                path.append(root.val)
                res.append([] + path)
                path.pop()
            return

        path.append(root.val)
        self.dfs(root.left, res, path, sum - root.val)
        self.dfs(root.right, res, path, sum - root.val)
        path.pop()