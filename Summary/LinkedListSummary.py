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


class Solution:
    def printList(self, head):
        while head is not None:
            print head.val
            head = head.next

    def getLenght(self, head):
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
        cur = head
        while cur is not None:
            preCur = cur
            cur = cur.next
            preCur.next = newhead
            newhead = preCur
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

a = Solution()
print a.getLastKth(head, 2).val
