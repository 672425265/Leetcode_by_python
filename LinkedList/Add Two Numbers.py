# coding: utf-8
'''
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        head = ListNode(0)
        point = head
        carry = 0
        while l1 is not None and l2 is not None:
            sum = carry + l1.val + l2.val
            point.next = ListNode(sum % 10)
            carry = sum / 10
            l1 = l1.next
            l2 = l2.next
            point = point.next

        while l1 is not None:
            sum = carry + l1.val
            point.next = ListNode(sum % 10)
            carry = sum / 10
            l1 = l1.next
            point = point.next

        while l2 is not None:
            sum = carry + l2.val
            point.next = ListNode(sum % 10)
            carry = sum / 10
            l2 = l2.next
            point = point.next

        if carry != 0:
            point.next = ListNode(carry)
        return head.next

class Solution2:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        l = head
        carry = 0
        while l1 or l2 or carry:
            sum, carry = carry, 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if sum > 9:
                carry = 1
                sum -= 10
            l.next = ListNode(sum)
            l = l.next
        return head.next