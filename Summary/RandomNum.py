import random
import sys
import collections

def withProbRandomPick(probList):
    r, s = random.random(), 0
    for num in probList:
        s += num[1]
        if s >= r:
            return num[0]
    print >> sys.stderr, "Error: "

probList = [[0, 0.6], [1, 0.4]]
count = collections.defaultdict(int)
# for i in xrange(10000):
#     count[withProbRandomPick(probList)] += 1
# for n in count:
#     print n, count[n] / 10000.0
print withProbRandomPick(probList)