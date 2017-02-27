
class Solution(object):
    def Fibonacci(self, n):
        if n <= 1:
            return n
        res = [0] * n
        res[0] = 0
        res[1] = 1
        for i in range(2, n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]