# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        self.dfs(res, path, root, sum)
        return res

    def dfs(self, res, path, root, sum):
        if root is None:
            return
        sum -= root.val
        if root.left is None and root.right is None:
            if sum == 0:
                path.append(root.val)
                res.append([] + path)
                path.pop()
            return
        path.append(root.val)
        self.dfs(res, path, root.left, sum)
        self.dfs(res, path, root.right, sum)
        path.pop()
