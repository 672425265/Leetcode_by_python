class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        length = len(nums)
        if nums is None or length == 0:
            return 0
        return self.helper(nums, 0, len(nums) - 1, len(nums) - k + 1)

    def helper(self, nums, l, r, k):
        if l == r:
            return nums[l]
        position = self.partition(nums, l, r)
        if position + 1 == k:
            return nums[position]
        elif position + 1 < k:
            return self.helper(nums, position + 1, r, k)
        else:
            return self.helper(nums, l, position - 1, k)

    def partition(self, nums, l, r):
        left = l
        right = r
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] > pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] < pivot:
                left += 1
            nums[right] = nums[left]

        nums[left] = pivot
        return left

solution = Solution()
print solution.findKthLargest([3,2,1,5,6,4], 2)