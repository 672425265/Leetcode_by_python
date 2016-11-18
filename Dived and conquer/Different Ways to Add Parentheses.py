# coding: utf-8
'''
Given a string of numbers and operators, return all possible results
from computing all the different possible ways to group numbers and operators.
The valid operators are +, - and *.
Example 1
Input: "2-1-1".
((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]
Example 2
Input: "2*3-4*5"
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
'''

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def calc(a, b, o):
            return {'+':lambda x,y:x+y, '-':lambda x,y:x-y, '*':lambda x,y:x*y}[o](a,b)
        res = []
        for i in range(len(input)):
            if input[i] == '-' or input[i] == '*' or input[i] == '+':
                part1 = input[0:i]
                part2 = input[i+1:]
                part1Res = self.diffWaysToCompute(part1)
                part2Res = self.diffWaysToCompute(part2)
                for p1 in part1Res:
                    for p2 in part2Res:
                        c = calc(p1, p2, input[i])
                        res.append(c)
        if len(res) == 0:
            res.append(int(input))
        return res

solution = Solution()
print solution.diffWaysToCompute("2*3-4*5")

