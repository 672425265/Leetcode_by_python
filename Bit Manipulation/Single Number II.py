# coding: utf-8

'''
Given an array of integers,
every element appears three times except for one. Find that single one.
'''

'''
如果我们把 第 ith 个位置上所有数字的和对3取余，
那么只会有两个结果 0 或 1 (根据题意，3个0或3个1相加余数都为0).
因此取余的结果就是那个 “Single Number”。
'''

# public class Solution {
#     public int singleNumber(int[] nums) {
#         int cnt[] = new int[32];
#         int single = 0;
#         for (int i = 0; i < 32; i++) {
#             for (int j = 0; j < nums.length; j++) {
#                 cnt[i] += (nums[j] >> i) & 0x1;
#             }
#             single |= cnt[i] % 3 << i;
#         }
#
#         return single;
#     }
# }

class Solution:
    def singleNumber(self, A):
        one = 0; two = 0; three = 0
        for i in range(len(A)):
            two |= A[i] & one
            one = A[i] ^ one
            three = ~(one & two)
            one &= three
            two &= three
        return one

solution = Solution()
print solution.singleNumber([-2,-2,-3,-3,-3,-4,-2])