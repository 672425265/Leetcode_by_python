# coding: utf-8

'''
A sequence of numbers is called a wiggle sequence if the differences
between successive numbers strictly alternate between positive and negative.
The first difference (if one exists) may be either positive or negative.
A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3)
are alternately positive and negative. In contrast, [1,4,7,2,5]
and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence
that is a wiggle sequence. A subsequence is obtained by deleting
some number of elements (eventually, also zero) from the original sequence,
leaving the remaining elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
'''

'''
一次遍历，将序列的连续递增部分和递减部分进行合并。
'''
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size < 2:
            return size
        delta = nums[1] - nums[0]
        ans = 1 + (delta != 0)
        for x in range(2, size):
            newDelta = nums[x] - nums[x-1]
            if newDelta != 0 and newDelta * delta <= 0:
                ans += 1
                delta = newDelta
        return ans


class Solution2(object):
    def wiggleMaxLength(self, nums):
        size = len(nums)
        inc = dec = 1
        for x in range(1, size):
            if nums[x] > nums[x - 1]:
                inc = dec + 1
            elif nums[x] < nums[x - 1]:
                dec = inc + 1
        return max(inc, dec) if size else 0

class Solution3(object):
    def wiggleMaxLength(self, nums):
        size = len(nums)
        inc, dec = [1] * size, [1] * size
        for x in range(1, size):
            if nums[x] > nums[x-1]:
                inc[x] = dec[x-1] + 1
                dec[x] = dec[x-1]
            elif nums[x] < nums[x-1]:
                inc[x] = inc[x-1]
                dec[x] = inc[x-1] + 1
            else:
                inc[x] = inc[x-1]
                dec[x] = dec[x-1]
        return max(inc[-1], dec[-1]) if size else 0

solution = Solution2()
print solution.wiggleMaxLength([1,2,3,4])