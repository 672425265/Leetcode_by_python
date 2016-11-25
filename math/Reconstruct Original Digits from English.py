# coding: utf-8
'''
Given a non-empty string containing an out-of-order English representation of digits 0-9,
output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits.
That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
'''

'''
字符统计 + 枚举

统计字符串s中各字符的个数，需要注意的是，在枚举英文字母时，需要按照特定的顺序方可得到正确答案。

例如按照顺序：6028745913，这个顺序可以类比拓扑排序的过程。

观察英文单词，six, zero, two, eight, seven, four中分别包含唯一字母x, z, w, g, v, u；因此6, 0, 2, 8, 7, 4需要排在其余数字之前。

排除这6个数字之后，剩下的4个数字中，按照字母唯一的原则顺次挑选。

由于剩下的单词中，只有five包含f，因此选为下一个单词；

以此类推，可以得到上面所述的顺序。
'''
from collections import Counter

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnts = Counter(s)
        nums = ['six', 'zero', 'two', 'eight', 'seven', 'four', 'five', 'nine', 'one', 'three']
        numc = [Counter(num) for num in nums]
        digits = [6, 0, 2, 8, 7, 4, 5, 9, 1, 3]
        ans = [0] * 10
        for idx, num in enumerate(nums):
            cntn = numc[idx]
            t = min(cnts[c] / cntn[c] for c in cntn)
            ans[digits[idx]] = t
            for c in cntn:
                cnts[c] -= t * cntn[c]
        return "".join(str(i) * n for i, n in enumerate(ans))

solution = Solution()
print solution.originalDigits("fviefuro")
