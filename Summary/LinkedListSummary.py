# coding: utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)
head.next = n1
n1.next = n2

head2 = ListNode(4)
n3 = ListNode(5)
n4 = ListNode(6)
head2.next = n3
n3.next = n4

class Solution:
    level = 1
    def printList(self, head):
        while head is not None:
            print head.val
            head = head.next

    def getLenghth(self, head):
        length = 0
        if head is None:
            return 0
        while head is not  None:
            head = head.next
            length += 1
        return length

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        newhead = None
        while head is not None:
            temp = head.next
            head.next = newhead
            newhead = head
            head = temp
        return newhead

    def getLastKth(self, head, k):
        if k == 0 or head is None:
            return None
        quick = head
        slow = head

        while k > 1 and quick is not None:
            quick = quick.next
            k -= 1

        if k > 1 or quick is None:
            return None

        while quick.next is not None:
            quick = quick.next
            slow = slow.next

        return slow

    def getMiddle(self, head):
        if head is None or head.next is None:
            return head
        quick = head
        slow = head

        while quick.next is not None and quick.next.next is not None:
            quick = quick.next
            slow = slow.next
        return slow

    def mergeTwoSortList(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        if head1.val < head2.val:
            mergeHead = head1
            head1 = head1.next
        else:
            mergeHead = head2
            head2 = head2.next
        cur = mergeHead
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
                cur = cur.next
            else:
                cur.next = head2
                head2 = head2.next
                cur = cur.next
        if head1 is not None:
            cur.next = head1
        elif head2 is not None:
            cur.next = head2

        return mergeHead


a = Solution()
# new = a.mergeTwoSortList(head, head2)
a.printList(head)
print "-----"
new = a.reverse(head)
a.printList(new)