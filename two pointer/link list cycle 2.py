# coding: utf-8

'''
Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.
Note: Do not modify the linked list.
Follow up:
Can you solve it without using extra space?
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        slow = head
        fast = head
        while True:
            if fast.next is None or fast.next.next is None:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        while head != slow:
            head = head.next
            slow = slow.next
        return head


head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(4)
head.next = p1
p1.next = p2
p2.next = p1

solution = Solution()
print solution.detectCycle(head)