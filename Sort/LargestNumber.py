'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        return str(int("".join(sorted([str(x) for x in nums],
                            cmp=lambda a, b: int(b + a) - int(a + b)))))


class Solution2:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        if len(num) == 0:
            return ""
        strAry = [str(item) for item in num]
        array = self.sorting(strAry)
        res = ''.join(array)
        if int(res) == 0:
            return '0'
        else:
            return res

    def sorting(self, strAry):
        for i in range(len(strAry) - 1):
            for j in range(i + 1, len(strAry)):
                if self.compare(strAry[i], strAry[j]):
                    temp = strAry[i]
                    strAry[i] = strAry[j]
                    strAry[j] = temp
        return strAry

    def compare(self, s1, s2):
        i1 = i2 = 0
        while i1 < len(s1) and i2 < len(s2):
            if s1[i1] < s2[i2]:
                return True
            elif s1[i1] > s2[i2]:
                return False
            else:
                i1 += 1
                i2 += 1
        if i1 < len(s1):
            return self.compare(s1[i1:], s2)
        if i2 < len(s2):
            return self.compare(s1, s2[i2:])
        return False

solution = Solution2()
a = solution.largestNumber([3, 30, 34, 5, 9])