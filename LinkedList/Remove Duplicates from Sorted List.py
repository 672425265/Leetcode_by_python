# coding: utf-8

'''
Given a sorted linked list, delete all duplicates such
that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        node = head
        while node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head

head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(2)
p3 = ListNode(2)
p4 = ListNode(4)
head.next = p1
p1.next = p2
p2.next = p3
p3.next = p4

solution = Solution()
solution.deleteDuplicates(head)
while head:
    print head.val
    head = head.next
