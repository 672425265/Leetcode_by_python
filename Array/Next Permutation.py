# coding: utf-8
'''
Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it
as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place, do not allocate extra memory.
Here are some examples. Inputs are in the left-hand column and
its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution(object):
    def reverse(self, nums, start, end):
        i, j = start, end
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = -1
        # 从最尾端开始往前寻找两个相邻的元素，两者满足i < ii（令第一个元素为i，第二个元素为ii）
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break
        # 如果没有找到这样的一对元素则，表明当前的排列是最大的，没有下一个大的排列
        if index == -1:
            self.reverse(nums, 0, len(nums) - 1)
            return
        # 如果找到，再从末尾开始找出第一个大于i的元素，记为biggerIndex
        biggerIndex = index + 1
        for i in range(len(nums) - 1, index, -1):
            if nums[i] > nums[index]:
                biggerIndex = i
                break

        # while biggerIndex - 1 > index and nums[biggerIndex] == nums[biggerIndex - 1]:
        #     biggerIndex -= 1

        nums[index], nums[biggerIndex] = nums[biggerIndex], nums[index]
        self.reverse(nums, index + 1, len(nums) - 1)

class Solution2:
    # @param nums: a list of integer
    # @return: return nothing (void), do not return anything, modify nums in-place instead
    def nextPermutation(self, nums):
        # write your code here
        i = len(nums)-1
        temp = []
        while i>0 and nums[i]<=nums[i-1]: i=i-1
        if i==0:
            for j in xrange(len(nums)-1, -1, -1): temp.append(nums[j])
            for j in xrange(len(nums)): nums[j] = temp[j]
            return
        for j in xrange(i-1): temp.append(nums[j])
        p = len(nums)-1
        while nums[p]<=nums[i-1]: p=p-1
        nums[p], nums[i-1] = nums[i-1], nums[p]
        temp.append(nums[i-1])
        for j in xrange(len(nums)-1, i-1, -1): temp.append(nums[j])
        for j in xrange(len(nums)): nums[j] = temp[j]
        return

solution = Solution2()
nums = [2,3,6,5,4,4]
solution.nextPermutation(nums)
print nums