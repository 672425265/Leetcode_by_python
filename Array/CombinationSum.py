# coding: utf-8
'''
Find all possible combinations of k numbers that
add up to a number n,
given that only numbers from 1 to 9 can be
used and each combination should be a unique set of numbers.

Example 1:
Input: k = 3, n = 7
Output:
[[1,2,4]]
Example 2:
Input: k = 3, n = 9
Output:
[[1,2,6], [1,3,5], [2,3,4]]
'''

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        stack = [(0, 1, [])]
        while stack:
            total, start, comb = stack.pop()
            if total == n and len(comb) == k:
                ans.append(comb)
                continue
            for i in range(start, 10):
                tmp_total = total + i
                if tmp_total > n:
                    break
                stack.append((tmp_total, i + 1, comb + [i]))
        return ans

solution = Solution()
print solution.combinationSum3(3)