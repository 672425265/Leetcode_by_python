# coding: utf-8

'''
Given an array S of n integers, are there elements
a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        '''
        题意：求数列中三个数之和为0的三元组有多少个，需去重
        暴力枚举三个数复杂度为O(N^3)
        先考虑2Sum的做法，假设升序数列a，对于一组解ai,aj, 另一组解ak,al
        必然满足 i<k j>l 或 i>k j<l, 因此我们可以用两个指针，
        初始时指向数列两端
        指向数之和大于目标值时，右指针向左移使得总和减小，反之左指针向右移
        由此可以用O(N)的复杂度解决2Sum问题，3Sum则枚举第一个数O(N^2)
        使用有序数列的好处是，在枚举和移动指针时值相等的数可以跳过，省去去重部分
        '''
        nums.sort()
        ans = []
        for i in xrange(len(nums) - 2):
            if i and nums[i] == nums[i - 1]:
                # 跳过重复的数字: 比如 [0,0,0,0]
                continue
            target = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == -1 * target:
                    ans.append([target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # 为了去重
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > -1 * target:
                    right -= 1
                elif nums[left] + nums[right] < -1 * target:
                    left += 1
        return ans

solution = Solution()
print solution.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])