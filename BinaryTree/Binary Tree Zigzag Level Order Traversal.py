# coding: utf-8
'''
Given a binary tree, return the zigzag level order traversal
of its nodes' values. (ie, from left to right,
then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        results = []
        if not root:
            return results
        q = [root]
        level = 1
        while q:
            new_q = []
            results.append([n.val for n in q])
            q.reverse()
            level += 1
            if level % 2 == 1:

                for node in q:
                    if node.left:
                        new_q.append(node.left)
                    if node.right:
                        new_q.append(node.right)
            else:
                for node in q:
                    if node.right:
                        new_q.append(node.right)
                    if node.left:
                        new_q.append(node.left)
            q = new_q

        return results

root = TreeNode(0)
root.left = TreeNode(4)
root.right = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(-1)
root.right.right = TreeNode(5)
# [3,9,20,null,null,15,7]
solution = Solution()
res = solution.zigzagLevelOrder(root)
print res