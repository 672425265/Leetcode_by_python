# coding: utf-8
'''
Given an array of strings, group anagrams together.
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = dict()
        for item in strs:
            itemstr = list(item)
            itemstr.sort()
            key = "".join(itemstr)
            if res.has_key(key):
                res[key].append(item)
            else:
                value = []
                value.append(item)
                res[key] = value
        ans = []
        for key in res:
            curr = res[key]
            ans.append(curr)
        return ans