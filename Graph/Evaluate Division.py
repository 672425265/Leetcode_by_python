# coding: utf-8

'''
Equations are given in the format A / B = k, where A and B are variables represented as strings,
and k is a real number (floating point number). Given some queries, return the answers.
If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
'''

'''
Floyd算法求解传递闭包

输入等式可以看做一个有向图

例如等式a / b = 2.0，可以转化为两条边：<a, b>，<b, a>，其长度分别为2.0，0.5

遍历equations与values，利用字典g保存有向图中各边的长度，g的keys即为顶点集

最后调用Floyd算法即可
'''

from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        g = defaultdict(lambda: defaultdict(int))
        for (s, t), v in zip(equations, values):
            g[s][t] = v
            g[t][s] = 1.0 / v
        for k in g:
            g[k][k] = 1.0
            for s in g:
                for t in g:
                    if g[s][k] and g[k][t]:
                        g[s][t] = g[s][k] * g[k][t]
        ans = []
        for s, t in queries:
            ans.append(g[s][t] if g[s][t] else -1.0)
        return ans