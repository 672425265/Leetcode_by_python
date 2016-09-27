# coding: utf-8

def quick_sort(arry):
    return qsort(arry, 0, len(arry)-1)

def qsort(arry, left, right):
    # arry为待排序数组,left为该数组左边界,right为该数组右边界
    if left >= right:
        return arry
    # 取最左边的数为基准数
    key = arry[left]
    lp = left
    rp = right
    while lp < rp:
        while arry[rp] >= key and lp < rp:
            rp -= 1
        while arry[lp] <= key and lp < rp:
            lp += 1
        arry[lp], arry[rp] = arry[rp], arry[lp]
    arry[left], arry[rp] = arry[rp], arry[left]
    qsort(arry, left, lp - 1)
    qsort(arry, rp + 1, right)
    return arry

print quick_sort([3,2,1,4])