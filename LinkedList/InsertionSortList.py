# coding: utf-8
'''
Sort a linked list using insertion sort.
Subscribe to see which companies asked this question
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr.next:
            if curr.next.val < curr.val:
                pre = dummy
                while pre.next.val < curr.next.val:
                    pre = pre.next
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp

            else:
                curr = curr.next
        return dummy.next
