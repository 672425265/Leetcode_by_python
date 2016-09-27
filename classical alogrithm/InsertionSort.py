# coding: utf-8

def insert_sort(arry):
    n = len(arry)
    for i in range(1, n):
        if arry[i] < arry[i-1]:
            temp = arry[i]
            index = i   # 待插入的下标
            for j in range(i-1, -1, -1): # 从i-1 循环到 0 (包括0)
                if arry[j] > temp:
                    arry[j+1] = arry[j]
                    index = j
                else:
                    break
            arry[index] = temp
    return arry

print insert_sort([3,2,1,4])