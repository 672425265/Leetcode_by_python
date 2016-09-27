# coding: utf-8

def select_sort(arry):
    n = len(arry)
    for i in range(0, n):
        min = i     # 先假定第一个为最小元素
        for j in range(i+1, n):
            if arry[j] < arry[min]:
                min = j     # 找到最小值的下标
        arry[min], arry[i] = arry[i], arry[min]
    return arry

print select_sort([3,2,1,4])