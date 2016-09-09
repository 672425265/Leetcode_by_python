def quickSort(nums, start, end):
    if start >= end:
        return
    left, right = start, end
    # key point 1: pivot is the value, not the index
    pivot = nums[(start + end) / 2]

    # key point 2: every time you compare
    # left & right, it should be
    while left <= right:
        # key point 3: A[left] < pivot not A[left] <= pivot
        while left <= right and nums[left] < pivot:
            left += 1
        # key point 3: A[right] > pivot not A[right] >= pivot
        while left <= right and nums[right] > pivot:
            right -= 1
        if left <= right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp

            left += 1
            right -= 1


nums = [2,1,3]
quickSort(nums,0, 2)
print nums