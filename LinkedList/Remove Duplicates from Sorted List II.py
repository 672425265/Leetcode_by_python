# coding: utf-8

'''
Given a sorted linked list,
delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        # 我们要删除一个点,必须要知道一个点的上一个是谁,必须先把head往回挪一个
        # 只有在dummy这个位置才能删除
        head = dummy

        while head.next and head.next.next:
            if head.next.val == head.next.next.val:
                val = head.next.val
                while head.next is not None and head.next.val == val:
                    head.next = head.next.next
            else:
                head = head.next

        return dummy.next

head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(2)
p3 = ListNode(4)
head.next = p1
p1.next = p2
p2.next = p3

solution = Solution()
solution.deleteDuplicates(head)
while head:
    print head.val
    head = head.next