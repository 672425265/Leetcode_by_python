# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        return self.judge(sequence, 0, len(sequence) - 1)

    def judge(self, sequence, l, r):
        if l >= r:
            return True
        i = r
        while i > l and sequence[i - 1] > sequence[r]:
            i -= 1
        for j in range(i - 1, l - 1, -1):
            if sequence[j] > sequence[r]:
                return False
        return self.judge(sequence, l, i - 1) and self.judge(sequence, i, r - 1)