# coding: utf-8
'''
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes
you can see ordered from top to bottom.
For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self, depthToValue, node, depth):
        if node is None:
            return
        depthToValue[depth] = node.val
        self.dfs(depthToValue, node.left, depth+1)
        self.dfs(depthToValue, node.right, depth+1)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        depthToValue = dict()
        self.dfs(depthToValue, root, 1)
        depth = 1
        res = []
        while depthToValue.has_key(depth):
            res.append(depthToValue[depth])
            depth += 1
        return res

class Solution2(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if root is None:
            return ans
        queue = [root]
        while queue:
            size = len(queue)
            for r in range(size):
                top = queue.pop(0)
                if r == 0:
                    ans.append(top.val)
                if top.right:
                    queue.append(top.right)
                if top.left:
                    queue.append(top.left)
        return ans