# coding: utf-8
'''
Given a linked list, swap every two adjacent nodes and return its head.
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space.
You may not modify the values in the list, only nodes itself can be changed.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next is not None and p.next.next is not None:
            n1 = p.next
            n2 = p.next.next
            p.next = n2
            n1.next = n2.next
            n2.next = n1
            p = n1
        return dummy.next

head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(4)
head.next = p1
p1.next = p2
p2.next = p3
solution = Solution()
solution.swapPairs(head)
while head:
    print head.val
    head = head.next
