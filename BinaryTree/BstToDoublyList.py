# coding: utf-8

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next

class Solution:
    """
    @param root, the root of tree
    @return: a doubly list node
    """
    def bstToDoublyList(self, root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        '''
        将左子树构成双链表,并返回链表头结点
        '''
        left = self.bstToDoublyList(root.left)
        p = left
        '''
        定位至左子树双链表的最后一个节点
        '''
        while p is not None and p.right is not None:
            p = p.right
        '''
        如果左子树链表不为空的话,将当前root追加到左子树链表
        '''
        if left is not None:
            p.right = root
            root.left = p
        '''
        将右子树构造双链表,并返回链表头结点
        '''
        right = self.bstToDoublyList(root.right)
        '''
        如果右子树链表不为空的话,将该链表追加到root节点之后
        '''
        if right is not None:
            right.left = root
            root.right = right
        if left is not None:
            return left
        else:
            return root