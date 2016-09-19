# coding: utf-8

'''
Given a string containing only digits,
restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",
return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        list = []
        if len(s) < 4 or len(s) > 12:
            return result
        self.helper(result, list, s, 0)
        return result

    def helper(self, result, list, s, start):
        if len(list) == 4:
            if start != len(s):
                return
            sb = ""
            for item in list:
                sb += item
                sb += "."
            sb = sb[:len(sb)-1]
            result.append(sb)
            return

        i = start
        while i < len(s) and i < start + 3:
            tmp = s[start:i + 1]
            if self.isvalid(tmp):
                list.append(tmp)
                self.helper(result, list, s, i + 1)
                list.pop()
            i += 1

    def isvalid(self, s):
        if s[0] == "0":
            return s == "0"
        digit = int(s)
        return digit >= 0 and digit <= 255

solution = Solution()
print solution.restoreIpAddresses("25525511135")