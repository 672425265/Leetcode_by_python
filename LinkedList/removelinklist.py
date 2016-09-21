# coding: utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNode(removedVal, head):
    if head is None:
        return head
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    while head:
        if head.val == removedVal:
            prev.next = head.next
            head = prev
        prev = head
        head = head.next
    return dummy.next

head = ListNode(1)
p1 = ListNode(2)      # 建立链表1->2->3->4->None;
p2 = ListNode(4)
p3 = ListNode(3)
head.next = p1
p1.next = p2
p2.next = p3

p = removeNode(2, head)
# while p:
#     print p.val
#     p = p.next