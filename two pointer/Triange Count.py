#codind: utf-8

'''
Given an array of integers, how many three numbers can be found
in the array so that we can build an triangle whose three edges
length is the three numbers that we find

Example
Given array S = [3, 4, 6, 7], return 3. They are
[3,4,6]
[3,6,7]
[4,6,7]
'''

'''
A[j] + A[k] > A[i]
'''
class Solution(object):
    def triangleCount(self, nums):
        nums.sort()
        ans = 0
        for i in xrange(len(nums)):
            target = nums[i]
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > target:
                    ans += (right - left)
                    right -= 1
                else:
                    left += 1
        return ans

solution = Solution()
print solution.triangleCount([3, 4, 6, 7])