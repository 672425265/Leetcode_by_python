# coding: utf-8

'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        if not head:
            return

        # find the mid point
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half in-place
        last, node = None, slow
        while node:
            last, node.next, node = node, last, node.next
            # nextNode = node.next
            # node.next = last
            # last = node
            # node = nextNode

        # Merge in-place; Note : the last node of "first" and "second" are the same
        first, second = head, last
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return
