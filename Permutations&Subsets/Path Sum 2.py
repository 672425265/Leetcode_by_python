# coding: utf-8

'''
Given a binary tree and a sum, find all root-to-leaf
paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSum(self, result, solution, root, sum):

        if root is None:
            return
        sum -= root.val

        if root.left is None and root.right is None:
            if sum == 0:
                solution.append(root.val)
                result.append(solution + [])
                solution.pop()
            return

        solution.append(root.val)
        self.findSum(result, solution, root.left, sum)
        self.findSum(result, solution, root.right, sum)
        solution.pop()


    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        rst = []
        solution = []
        self.findSum(rst, solution, root, sum)
        return rst
