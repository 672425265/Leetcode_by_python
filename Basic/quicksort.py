def quick(nums):
    quickSort(nums, 0, len(nums) - 1)
    return nums

def quickSort(nums, left, right):
    l, r = left, right
    if l >= r:
        return nums
    pivot = (left + right) / 2
    while l <= r:
        while nums[l] < nums[pivot]:
            l += 1
        while nums[r] > nums[pivot]:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    quickSort(nums, left, r)
    quickSort(nums, l, right)

nums = [2,9,3,1,6,9,6]
quick(nums)
print nums