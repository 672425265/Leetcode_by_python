# coding: utf-8

def bubble_sort(arry):
    n = len(arry)   # 获得数组的长度
    for i in range(n):
        for j in range(i + 1, n):
            if arry[i] > arry[j]:   # 如果前者比后者大
                arry[i], arry[j] = arry[j], arry[i] # 则互相交换
    return arry

print bubble_sort([3,2,1,4])
