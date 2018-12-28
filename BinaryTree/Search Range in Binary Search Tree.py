# coding: utf-8

'''
Given two values k1 and k2 (where k1 < k2)
and a root pointer to a Binary Search Tree.
Find all the keys of tree in range k1 to k2.
i.e. print all x such that k1<=x<=k2 and x
is a key of given BST. Return all the keys in ascending order.
'''


class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        ans = []
        if root is None:
            return ans
        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index] is not None:
                if queue[index].val > k1 and queue[index].val <= k2:
                    ans.append(queue[index].val)
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1
        return sorted(ans)
