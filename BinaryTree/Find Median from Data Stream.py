# coding: utf-8
'''
Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports
the following two operations:

void addNum(int num) - Add a integer number
from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3)
findMedian() -> 2
'''

from heapq import *

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []

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

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.maxHeap) == len(self.minHeap):
            return (-1 * self.maxHeap[0] + self.minHeap[0]) * 0.5
        else:
            return -1 * self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
mf.addNum(3)
mf.addNum(4)
mf.addNum(5)
print mf.findMedian()