# coding: utf-8

'''
Design an iterator over a binary search tree
with the following rules:

Elements are visited in ascending order
(i.e. an in-order traversal)
next() and hasNext() queries run in O(1) time in average.
'''

class BSTIterator:
    #@param root: The root of binary tree.
    def __init__(self, root):
        # write your code here
        self.stack = []
        self.curt = root

    #@return: True if there has next node, or false
    def hasNext(self):
        # write your code here
        return self.curt is not None or len(self.stack) > 0

    #@return: return next node
    def next(self):
        #write your code here
        while self.curt is not None:
            self.stack.append(self.curt)
            self.curt = self.curt.left
        self.curt = self.stack.pop()
        nxt = self.curt
        self.curt = self.curt.right
        return nxt.val

