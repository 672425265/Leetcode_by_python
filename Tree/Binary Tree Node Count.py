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
        return 1 + self.nodeSum(root.left) + self.nodeSum(root.right)


class Solution2(object):
    def nodeSum(self, root):
        if root is None:
            return 0
        leftSum = self.nodeSum(root.left)
        rightSum = self.nodeSum(root.right)

        return 1 + leftSum + rightSum


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    res = 0
    print Solution2().nodeSum(root)