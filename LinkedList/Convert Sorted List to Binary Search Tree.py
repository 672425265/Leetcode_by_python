# coding: utf-8
'''
Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self, head):
        if head is None:
            return None

        if head.next is None:
            return TreeNode(head.val)

        dummy = ListNode(0)
        dummy.next = head
        fast = head
        slow = dummy

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        parent = TreeNode(temp.val)
        parent.left = self.dfs(head)
        parent.right = self.dfs(temp.next)

        return parent

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        res = self.dfs(head)
        return res
