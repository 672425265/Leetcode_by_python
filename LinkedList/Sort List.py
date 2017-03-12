# coding: utf-8

'''
Sort a linked list in O(n log n) time using constant space complexity.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def findMiddle(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(self, head1, head2):
        dummy = ListNode(0)
        tail = dummy
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        if head1 is not None:
            tail.next = head1
        else:
            tail.next = head2

        return dummy.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        mid = self.findMiddle(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)

        return self.merge(left, right)

head = ListNode(4)
p1 = ListNode(2)      # 建立链表1->2->3->4->None;
p2 = ListNode(2)
p3 = ListNode(1)
head.next = p1
p1.next = p2
p2.next = p3

solution = Solution()
p = solution.sortList(head)
while p:
    print p.val
    p = p.next
