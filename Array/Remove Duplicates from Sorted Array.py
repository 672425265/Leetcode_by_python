# coding: utf-8

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        i, j = 1, 0
        # i指向要拷贝的节点, j指向当前扫描到的节点
        while i < len(nums):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
            i += 1
        return j+1

solution = Solution()
nums = [1, 2, 2]
len = solution.removeDuplicates(nums)
print len
