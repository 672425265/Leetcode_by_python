#coding: utf-8

'''
Given a linked list, remove the nth node
from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end,
   the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        first, second = head, dummy
        for i in range(n):
            first = first.next
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(2)
p3 = ListNode(4)
head.next = p1
p1.next = p2
p2.next = p3

solution = Solution()
solution.removeNthFromEnd(head, 1)
while head:
    print head.val
    head = head.next