def quick(nums):
    return quickSort(nums, 0, len(nums) - 1)

def quickSort(nums, left, right):
    if left >= right:
        return nums
    pivot = nums[left]
    l, r = left, right
    while l <= r:
        while l <= r and nums[r] > pivot:
            r -= 1
        while l <= r and nums[l] < pivot:
            l += 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    quickSort(nums, left, r)
    quickSort(nums, l, right)
    return nums

nums = [19,-10,-2,40,3,36,57,25,66,51,5,40,-8,43,9,-5,0,4]
quick(nums)
print nums