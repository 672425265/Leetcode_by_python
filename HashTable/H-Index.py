# coding: utf-8

'''
Given an array of citations (each citation
is a non-negative integer) of a researcher,
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia:
"A scientist has index h if h of his/her N papers have
at least h citations each, and the other N − h papers
have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5],
which means the researcher has 5 papers in total
and each of them had received 3, 0, 6, 1, 5 citations
respectively. Since the researcher has 3 papers with
at least 3 citations each and the remaining two with n
o more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h,
the maximum one is taken as the h-index.

'''


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        for i in xrange(len(citations)):
            if i >= citations[i]:
                return i
        return len(citations)

class Solution2(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        stats = [0] * (len(citations) + 1)
        '''
        统计各个引用次数对应多少篇文章
        '''
        for i in xrange(len(citations)):
            if citations[i] > len(citations):
                stats[len(citations)] += 1
            else:
                stats[citations[i]] += 1
        sum = 0
        for i in xrange(len(citations), 0, -1):
            '''
            引用大于等于i次的文章数量，等于引用大于等于i + 1
            次的文章数量，加上引用等于i次的文章数量
            '''
            sum += stats[i]
            '''
            如果引用大于等于i次的文章数量，大于引用次数i，说明是H指数
            '''
            if sum >= i:
                return i
        return 0

solution = Solution2()
print solution.hIndex([0])