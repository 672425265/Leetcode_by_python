# coding: utf-8
'''
You are given two linked lists representing two non-negative numbers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
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
        def getSize(h):
            c = 0
            while h:
                c += 1
                h = h.next
            return c
        s1 = getSize(l1)
        s2 = getSize(l2)
        s = max(s1, s2)

        p = h = ListNode(0)
        while s:
            p.next = ListNode(0)
            p = p.next
            if s <= s1:
                p.val += l1.val
                l1 = l1.next
            if s <= s2:
                p.val += l2.val
                l2 = l2.next
            s -= 1

        p = h
        while p:
            q = p.next
            while q and q.val == 9:
                q = q.next
            if q and q.val > 9:
                while p != q:
                    p.val += 1
                    p = p.next
                    p.val -= 10
            else:
                p = q
        return h if h.val else h.next