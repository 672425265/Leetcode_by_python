# coding: utf-8


def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
      if left[l] < right[r]:
          result.append(left[l])
          l += 1
      else:
          result.append(right[r])
          r += 1
    result += left[l:]
    result += right[r:]
    return result


def merge_sort(arry):
    n = len(arry)
    if n <= 1:
        return arry
    num = n/2
    left = merge_sort(arry[:num])
    right = merge_sort(arry[num:])
    return merge(left, right)


print merge_sort([3,2,1,4])