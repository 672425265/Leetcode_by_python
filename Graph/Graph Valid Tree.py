class Solution:
    def validTree(self, n, edges):
        if n == 0:
            return False
        if len(edges) != n - 1:
            return False
        graph = self.initializeGraph(n, edges)
        queue = []
        hashset = set()
        queue.append(0)
        hashset.add(0)
        while len(queue) > 0:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if neighbor in hashset:
                    continue
                hashset.add(neighbor)
                queue.append(neighbor)
        return len(hashset) == n

    def initializeGraph(self, n, edges):
        graph = {}
        for i in range(n):
            graph[i] = set()

        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            graph[u].add(v)
            graph[v].add(u)

        return graph

s = Solution()
n = 4
edges = [[0,1],[1,2],[0,2]]
print s.validTree(n, edges)