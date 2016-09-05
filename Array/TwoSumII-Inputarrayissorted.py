# coding: utf-8

'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        last = len(numbers) - 1
        while start != last:
            sum = numbers[start] + numbers[last]
            if sum == target:
                return [start+1, last+1]
            elif sum < target:
                start += 1
            else:
                last -= 1
        return

solution = Solution()
ans = solution.twoSum([5,25,75], 100)
print ans