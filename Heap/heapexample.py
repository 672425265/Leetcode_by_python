# coding: utf-8
from heapq import *

'''
heappush(heap, item): 将item压入堆数组heap中。
必须先进行此步操作,后面的heappop才有效。

heappop(heap): 从堆数组heap中取出最小的值,并返回。
'''
def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


# 输出: [1, 2, 3, 3, 7]
print heapsort([1, 3, 7, 3, 2])


'''
heappushpop(heap, item)
增加item的同时删除最小值,并且返回该堆的最小值
'''
def example(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    a = heappop(h)
    # 增加4的同时删除最小值,并且返回该最小值
    b = heappushpop(h, 4)
    print a
    print b
    print h

# 输出: 1
# 输出: 2
# 输出: [4, 5, 9]
example([1, 2, 9, 5])

'''
heapify(x)
x必须是list，此函数将list变成堆，实时操作。从而能够在任何情况下使用堆的函数。
'''
def example2(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    heapify(h)
    print h

# 输出: [1, 6, 3]
example2([3, 6, 1])

'''
heapreplace(heap, item)
先进行删除,后压入栈
'''
def example3():
    a = []
    heappush(a, 3)
    # 输出: [3]
    print a
    # 先执行删除（heappop(a)->3),再执行加入（heappush(a,4))
    heapreplace(a, 4)
    # 输出: [4]
    print a

'''
归并排序
merge(*iterables)
'''
def example4():
    a = [2,4,6]
    b = [1,3,5]
    c = merge(a, b)
    # 输出: [1, 2, 3, 4, 5, 6]
    print list(c)

'''
nlargest(n, iterable[, key]), nsmallest(n, iterable[, key])
获取列表中最大、最小的几个值。
'''
def example5():
    a = [1, 3, 4, 2]
    # 输出: [4, 3]
    print nlargest(2, a)
    # 输出: [1, 2]
    print nsmallest(2, a)

