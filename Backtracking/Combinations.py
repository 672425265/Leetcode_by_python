class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        rst = []
        solution = []
        self.dfs(rst, solution, n, k, 1)
        return rst

    def dfs(self, rst, solution, n, k, start):
        if len(solution) == k:
            rst.append(solution + [])

        if n - start + 1 < k - len(solution):
            return

        for i in range(start, n + 1):
            solution.append(i)
            self.dfs(rst, solution, n, k, i + 1)
            solution.pop()

