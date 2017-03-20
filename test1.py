# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root
        nums = self.InOrder(root)
        print nums
        hashmap = {}
        for i in range(len(nums) - 1):
            value = nums[i] + sum(nums[i + 1:])
            hashmap[nums[i]] = value

        hashmap[nums[len(nums) - 1]] = nums[len(nums) - 1]
        print hashmap
        self.helper(root, hashmap)
        return root

    def helper(self, root, hashmap):
        if root is None:
            return
        root.val = hashmap[root.val]
        self.helper(root.left, hashmap)
        self.helper(root.right, hashmap)

    def InOrder(self, root):
        stack = []
        res = []
        if root is None:
            return res
        cur = root
        while cur is not None or len(stack) > 0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

tree = TreeNode(2)
tree.left = TreeNode(1)
# tree.right = TreeNode(3)

s = Solution()
s.convertBST(tree)
root = s.convertBST(tree)
print root.val
print root.left.val