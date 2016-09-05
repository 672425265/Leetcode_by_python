# coding: utf-8

'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.level_dfs(root, 0, result)
        return result

    def level_dfs(self, node, level, result):
        if not node:
            return
        if level == len(result):
            result.append([])
        result[level].append(node.val)
        self.level_dfs(node.left, level+1, result)
        self.level_dfs(node.right, level+1, result)


    def levelOrder2(self, root):
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans