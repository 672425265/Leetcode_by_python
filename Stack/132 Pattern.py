# coding: utf-8

'''
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak
such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers
as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
'''

'''
那么我们就按顺序来找这三个数，首先我们来找第一个数，这个数需要最小，
那么我们如果发现当前数字大于等于后面一个数字，我们就往下继续遍历，直到当前数字小于下一个数字停止。
然后我们找第二个数字，这个数字需要最大，那么如果我们发现当前数字小于等于下一个数字就继续遍历，
直到当前数字大雨下一个数字停止。最后就找第三个数字，我们验证这个数字是否在之前两个数字的中间，
如果没有找到，我们就从第二个数字的后面一个位置继续开始重新找这三个数字
'''

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return False
        n, i, j, k = len(nums), 0, 0, 0
        while i < n:
            while i < n - 1 and nums[i] >= nums[i + 1]:
                i += 1
            j = i + 1
            while j < n - 1 and nums[j] <= nums[j + 1]:
                j += 1
            k = j + 1
            while k < n:
                if nums[k] > nums[i] and nums[k] < nums[j]:
                    return True
                k += 1
            i = j + 1
        return False

import sys

'''
思路是我们维护一个栈和一个变量third，其中third就是第三个数字，也是pattern 132中的2，栈里面按顺序放所有大于third的数字，
也是pattern 132中的3，那么我们在遍历的时候，如果当前数字小于third，即pattern 132中的1找到了，
我们直接返回true即可，因为已经找到了，注意我们应该从后往前遍历数组。如果当前数字大于栈顶元素，
那么我们按顺序将栈顶数字取出，赋值给third，然后将该数字压入栈，这样保证了栈里的元素仍然都是大于third的，
我们想要的顺序依旧存在，进一步来说，栈里存放的都是可以维持second > third的second值，其中的任何一个值都是大于当前的third值，
如果有更大的值进来，那就等于形成了一个更优的second > third的这样一个组合，并且这时弹出的third值比以前的third值更大，
为什么要保证third值更大，因为这样才可以更容易的满足当前的值first比third值小这个条件
'''
class Solution2(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        third = -1 * sys.maxint
        s = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < third:
                return True
            else:
                while s is not None and nums[i] > s[-1]:
                    third = s[-1]
                    s.pop()
            s.append(nums[i])
        return False

solution = Solution()
print solution.find132pattern([-1, 3, 2, 0])