class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        res = []
        path = []
        self.dfs(root, res, path, sum)
        return res

    def dfs(self, root, res, path, sum):
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
        self.dfs(root.left, res, path, sum - root.val)
        self.dfs(root.right, res, path, sum - root.val)
        path.pop()