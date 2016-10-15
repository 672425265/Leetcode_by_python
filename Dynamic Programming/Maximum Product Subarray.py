# coding: utf-8
'''
Find the contiguous subarray within
an array (containing at least one number)
which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count_1: max
        # count_2: min
        length = len(nums)
        count_1 = [0] * length
        count_2 = [0] * length
        count_1[0] = nums[0]
        count_2[0] = nums[0]
        result = nums[0]
        for i in xrange(1, length):
            count_1[i] = nums[i]
            count_2[i] = nums[i]
            if nums[i] > 0:
                count_1[i] = max(count_1[i], nums[i] * count_1[i - 1])
                count_2[i] = min(count_2[i], nums[i] * count_2[i - 1])
            elif nums[i] < 0:
                count_1[i] = max(count_1[i], nums[i] * count_2[i - 1])
                count_2[i] = min(count_2[i], nums[i] * count_1[i - 1])
            result = max(result, count_1[i])
        return result

class Solution2:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        # write your code here
        f, g = [], []
        f.append(nums[0])
        g.append(nums[0])
        for i in xrange(1, len(nums)):
            f.append(max(f[i-1]*nums[i], g[i-1]*nums[i], nums[i]))
            g.append(min(f[i-1]*nums[i], g[i-1]*nums[i], nums[i]))
        m = f[0]
        for i in xrange(1, len(f)):
            m = max(m, f[i])
        return m

solution = Solution()
print solution.maxProduct([2,3,-2,4])