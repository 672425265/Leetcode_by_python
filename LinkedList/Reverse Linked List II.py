# coding: utf-8
'''
Reverse a linked list from position m to n.
Do it in-place and in one-pass.
For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,
return 1->4->3->2->5->NULL.
Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m >= n and head is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        for i in range(1, m):
            if head is None:
                return None
            head = head.next

        premNode = head
        mNode = head.next
        nNode, postnNode = mNode, mNode.next
        for i in range(m, n):
            temp = postnNode.next
            postnNode.next = nNode
            nNode = postnNode
            postnNode = temp
        mNode.next = postnNode
        premNode.next = nNode

        return dummy.next