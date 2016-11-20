# coding: utf-8
'''
All DNA is composed of a series of nucleotides abbreviated
as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA,
it is sometimes useful to identify repeated sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings)
that occur more than once in a DNA molecule.
For example,
Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
Return:
["AAAAACCCCC", "CCCCCAAAAA"].
'''

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def encode(s):
            sum = 0
            for i in range(0, len(s)):
                if s[i] == 'A':
                    sum = sum * 4
                elif s[i] == 'C':
                    sum = sum * 4 + 1
                elif s[i] == 'G':
                    sum = sum * 4 + 2
                else:
                    sum = sum * 4 + 3
            return sum

        hash = set()
        dna = set()
        for i in range(9, len(s)):
            subString = s[i-9:i+1]
            encoded = encode(subString)
            if encoded in hash:
                dna.add(subString)
            else:
                hash.add(encoded)
        result = []
        for item in dna:
            result.append(item)
        return result

class Solution2(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        dic={}
        ret=[]
        for i in range(len(s)-9):
            if s[i:i+10] not in dic:
                dic[s[i:i+10]]=1
            elif dic[s[i:i+10]]==1 and s[i:i+10] not in ret:
                ret.append(s[i:i+10])
        return ret

solution = Solution2()
print solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
