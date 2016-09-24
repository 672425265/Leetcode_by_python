# coding: utf-8
'''
A linked list is given such that each node
contains an additional random pointer
which could point to any node in the list or null.
Return a deep copy of the list.
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution():
    def copyNext(self, head):
        while head:
            newNode = RandomListNode(head.label)
            newNode.random = head.random
            newNode.next = head.next
            head.next = newNode
            head = head.next.next

    def copyRandom(self, head):
        while head:
            if head.next.random is not None:
                head.next.random = head.random.next
            head = head.next.next

    def splitList(self, head):
        newHead = head.next
        while head:
            temp = head.next
            head.next = temp.next
            head = head.next
            if temp.next is not None:
                temp.next = temp.next.next
        return newHead

    def copyRandomList(self, head):
        if head is None:
            return None
        self.copyNext(head)
        self.copyRandom(head)
        return self.splitList(head)

solution = Solution()
