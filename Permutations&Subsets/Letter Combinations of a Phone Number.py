# coding: utf-8

'''
Given a digit string,
return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons)
is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''


class Solution(object):
    def helper(self, map, digits, sb, result):
        if len(sb) == len(digits):
            result.append(sb)
            return
        for key in map[digits[len(sb)]]:
            sb += key
            self.helper(map, digits, sb, result)
            sb = sb[0:len(sb) - 1]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        if digits is None or len(digits) == 0:
            return result
        map = dict()
        map["0"] = []
        map["1"] = []
        map["2"] = ["a", "b", "c"]
        map["3"] = ["d", "e", "f"]
        map["4"] = ["g", "h", "i"]
        map["5"] = ["j", "k", "l"]
        map["6"] = ["m", "n", "o"]
        map["7"] = ["p", "q", "r", "s"]
        map["8"] = ["t", "u", "v"]
        map["9"] = ["w", "x", "y", "z"]

        sb = ""
        self.helper(map, digits, sb, result)

        return result

solution = Solution()
print solution.letterCombinations("23")