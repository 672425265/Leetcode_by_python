# coding: utf-8

'''
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space.

The input size may be as large as 5,000,000.
'''

# class Solution(object):
#     def lexicalOrder(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
#         """
#         result = []
#         def solve(m):
#             result.append(m)
#             if m * 10 <= n: solve(m * 10)
#             if m < n and m % 10 < 9: solve(m + 1)
#         solve(1)
#         return result

'''
优先将数字乘10；如果数字末位＜9，考虑将数字加1
递归式类似于二叉树的先根遍历
'''
class Solution(object):
    def lexicalOrder(self, n):
        result = []
        stack = [1]
        while stack:
            y = stack.pop()
            result.append(y)
            if y < n and y % 10 < 9:
                stack.append(y + 1)
            if y * 10 <= n:
                stack.append(y * 10)
        return result

solution = Solution()
print solution.lexicalOrder(9)