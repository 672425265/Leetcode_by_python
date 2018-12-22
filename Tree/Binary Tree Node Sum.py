# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def nodeSum(self, root):
        if root is None:
            return 0
        return root.val + self.nodeSum(root.left) + self.nodeSum(root.right)


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    res = 0
    print Solution().nodeSum(root)