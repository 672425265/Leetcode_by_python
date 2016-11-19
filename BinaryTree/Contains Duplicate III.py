# coding: utf- 8
'''
Given an array of integers, find out whether there are two distinct
indices i and j in the array such that the difference between nums[i]
and nums[j] is at most t and the difference
between i and j is at most k.
'''
# 如果： | nums[i] - nums[j] | <= t
# 等价： | nums[i] / t - nums[j] / t | <= 1
# 推出： | floor(nums[i] / t) - floor(nums[j] / t) | <= 1
# ​等价： floor(nums[j] / t) ∈ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1}
# 其中式b是式c的充分非必要条件，因为逆否命题与原命题等价，所以：
# 如果： floor(nums[j] / t) ∉ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1} 非d
# 推出： | nums[i] - nums[j] | > t   非a
# 因此只需要维护一个大小为k的窗口（字典）numDict，其中键为nums[i] / t，值为nums[i]。
# 遍历数组nums时，检查nums[i]与键集{floor(nums[i] / t) - 1, floor(nums[i] / t),
# floor(nums[i] / t) + 1}对应的值的差值即可。

from collections import OrderedDict

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        numDict = OrderedDict()
        for x in range(len(nums)):
            key = nums[x] / max(1, t)
            for m in (key, key - 1, key + 1):
                if m in numDict and abs(nums[x] - numDict[m]) <= t:
                    return True
            numDict[key] = nums[x]
            if x >= k:
                numDict.popitem(last=False)
        return False
