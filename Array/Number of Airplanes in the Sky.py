#coding: utf-8

'''
Given an interval list which are flying
and landing time of the flight.
How many airplanes are on the sky at most?

If landing and flying happens at the same time,
we consider landing should happen at first.
Example
For interval list
[
  [1,10],
  [2,3],
  [5,8],
  [4,7]
]
Return 3
'''
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
def sorter(x, y):
    if x[0] != y[0]:
        return x[0] - y[0]
    return x[1] - y[1]

class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        timepoints = []
        for airplane in airplanes:
            timepoints.append((airplane.start, 1))
            timepoints.append((airplane.end, -1))

        timepoints = sorted(timepoints, cmp=sorter)
        sum, most = 0, 0
        for t, delta in timepoints:
            sum += delta
            most = max(most, sum)

        return most

