# coding: utf-8

def shell_sort(arry):
    n = len(arry)
    gap = n/2    # 初始步长
    while gap > 0:
        for i in range(gap, n):     # 对每一列进行插入排序, 从gap 到 n-1
            temp = arry[i]
            j = i
            while j >= gap and arry[j-gap] > temp: # 插入排序
                arry[j] = arry[j-gap]
                j -= gap
            arry[j] = temp
        gap /= 2
    return arry

print shell_sort([3,2,1,4,5])
