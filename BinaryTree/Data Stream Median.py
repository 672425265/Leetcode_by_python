# coding: utf-8
'''
数字是不断进入数组的，
在每次添加一个新的数进入数组的同时返回当前新数组的中位数。

说明
中位数的定义：

中位数是排序后数组的中间值，如果有数组中有n个数，则中位数为A[(n-1)/2]。
比如：数组A=[1,2,3]的中位数是2，数组A=[1,19]的中位数是1。
样例
持续进入数组的数的列表为：[1, 2, 3, 4, 5]，则返回[1, 1, 2, 2, 3]

持续进入数组的数的列表为：[4, 5, 1, 3, 2, 6, 0]，则返回 [4, 4, 4, 3, 3, 3, 3]

持续进入数组的数的列表为：[2, 20, 100]，则返回[2, 2, 20]
'''

from heapq import *

class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    maxHeap, minHeap = [], []
    numbers = 0
    def addNum(self, num):
        """
        Adds a num into the Find Median from Data Streamdata structure.
        :type num: int
        :rtype: void
        """
        heappush(self.maxHeap, -num)
        # minTop 存放 右半部分的元素
        minTop = self.minHeap[0] if len(self.minHeap) else None
        # maxTop 存放 左半部分的元素
        maxTop = -1 * self.maxHeap[0] if len(self.maxHeap) else None
        if minTop < maxTop or len(self.minHeap) + 1 < len(self.maxHeap):
            heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -1 * heappop(self.minHeap))

    def getMedian(self):
        return -self.maxHeap[0]

    def medianII(self, nums):
        ans = []
        for item in nums:
            self.addNum(item)
            ans.append(self.getMedian())
        return ans

