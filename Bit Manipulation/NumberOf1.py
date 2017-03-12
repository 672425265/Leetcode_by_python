
class Solution:
    def numberOf1(self, n):
        count = 0
        for i in xrange(32):
            count += n & 1
            n >> 1
        return count

s = Solution()
print s.numberOf1(1)