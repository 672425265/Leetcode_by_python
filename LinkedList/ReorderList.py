# coding: utf-8

'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def findmiddle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self, head):
        pre = None

        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp

        return pre

    def merge(self, head1, head2):
        dummy = ListNode(0)
        index = 0
        while head1 and head2:
            if index % 2 == 0:
                dummy.next = head1
                head1 = head1.next
            else:
                dummy.next = head2
                head2 = head2.next
            dummy = dummy.next
            index += 1

        if head1 is not  None:
            dummy.next = head1
        else:
            dummy.next = head2

    def reorderList(self, head):
        if head is None or head.next is None:
            return
        mid = self.findmiddle(head)
        second = self.reverse(mid.next)
        mid.next = None
        self.merge(head, second)

head = ListNode(1)
p1 = ListNode(2)      
p2 = ListNode(3)
p3 = ListNode(4)
head.next = p1
p1.next = p2
p2.next = p3

solution = Solution()
solution.reorderList(head)
while head:
    print head.val
    head = head.next

