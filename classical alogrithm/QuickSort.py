# coding: utf-8


def quick_sort(arry):
    return qsort(arry, 0, len(arry)-1)


def qsort(array, left, right):
    # array 为待排序数组, left 为该数组左边界, right 为该数组右边界
    if left >= right:
        return array
    # 取最左边的数为基准数
    key = array[left]
    lp = left
    rp = right
    while lp < rp:
        while array[rp] >= key and lp < rp:
            rp -= 1
        while array[lp] <= key and lp < rp:
            lp += 1
        array[lp], array[rp] = array[rp], array[lp]
    array[left], array[rp] = array[rp], array[left]
    qsort(array, left, lp - 1)
    qsort(array, rp + 1, right)
    return array


print quick_sort([3, 2, 2, 2, 1, 4])