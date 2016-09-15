# coding: utf-8
'''
Given a set of distinct integers, nums,
return all possible subsets.
Note: The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.results = []
        self.search(sorted(nums), [], 0)
        return self.results

    def search(self, nums, S, index):
        if index == len(nums):
            self.results.append(S)
            return
        self.search(nums, S + [nums[index]], index + 1)
        self.search(nums, S, index + 1)


class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        if nums is None or len(nums) == 0:
            return result
        nums.sort()
        for num in nums:
            result += [item + [num] for item in result]
        return result


class Solution3(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if nums is None or len(nums) == 0:
            return result
        nums.sort()
        self.subsetshelper([], nums, 0, result)
        return result

    def subsetshelper(self, list, nums, pos, result):
        result.append([] + list)
        for i in xrange(pos, len(nums)):
            list.append(nums[i])
            self.subsetshelper(list, nums, i + 1, result)
            list.pop()


class Solution4(object):
    def subsets(self, nums):
        if nums is None or len(nums) == 0:
            return []
        result = []
        nums.sort()
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, pos, list_temp, ret):
        ret.append([] + list_temp)

        for i in xrange(pos, len(nums)):
            list_temp.append(nums[i])
            self.dfs(nums, i + 1, list_temp, ret)
            list_temp.pop()

solution = Solution3()
print solution.subsets([1,2,3])