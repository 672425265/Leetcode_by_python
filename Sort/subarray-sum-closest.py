# coding: utf-8class Node:
class Node:
    def __init__(self, _value, _pos):
        self.value = _value
        self.pos = _pos
    def __cmp__(self, other):
        if self.value == other.value:
            return self.pos - other.pos
        return self.value - other.value

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        s = []
        s.append(Node(0, -1))
        sum = 0
        for x in xrange(len(nums)):
            sum += nums[x]
            s.append(Node(sum, x))

        s = sorted(s)
        results = [0, 0]
        ans = 1000000000000
        for i in xrange(len(s) - 1):
            if s[i + 1].value - s[i].value <= ans or \
                                            s[i + 1].value - s[i].value == ans and \
                                            min(s[i + 1].pos, s[i].pos) + 1 < results[0]:
                ans = s[i + 1].value - s[i].value
                results[0] = min(s[i + 1].pos, s[i].pos) + 1
                results[1] = max(s[i + 1].pos, s[i].pos)

        return results
'''
给定一个整数数组，找到一个和最接近于零的子数组。
返回第一个和最有一个指数。
你的代码应该返回满足要求的子数组的起始位置和结束位置
样例:
给出[-3, 1, 1, -3, 5]，返回[0, 2]，[1, 3]， [1, 1]， [2, 2] 或者 [0, 4]。
'''



solution = Solution()
print solution.subarraySumClosest([-3, 1, 1, -3, 5])