# coding: utf-8

def heap_sort(arr, k):
    top = k
    n = len(arr)
    # 最后一个非叶子节点
    first = int(n/2-1)
    # 构造大根堆
    for start in range(first, -1, -1):
        max_heapify(arr, start, n - 1)
    for end in range(n-1, 0, -1):
        # 堆排，将大根堆转换成有序数组
        if k > 0:
            arr[end], arr[0] = arr[0], arr[end]
            max_heapify(arr, 0, end - 1)
            k -= 1
        else:
            break
    return arr[n - top:]

# 最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
# start为当前需要调整最大堆的位置，end为调整边界

def max_heapify(arr, start, end):
    root = start
    while True:
        # 调整节点的子节点
        child = root*2 + 1
        if child > end:
            break
        if child+1 <= end and arr[child] < arr[child+1]:
            # 取较大的子节点
            child += 1
        # 较大的子节点成为父节点
        if arr[root] < arr[child]:
            # 交换
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break

print heap_sort([3, 1, 4, 9, 6, 7, 5, 8, 2, 10], 3)