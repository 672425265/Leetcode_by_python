class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[1 << 32] * n for _ in range(m)]
    dp[0][0] = grid[0][0]

    for i in range(n):
        for j in range(m):
            if grid[i][j] != "x":
                bfs(grid, dp, i, j)

    return dp[m - 1][n - 1]


def bfs(grid, dp, x, y):
    direX = [1, 0, 0, -1]
    direY = [0, -1, 1, 0]
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    visited[x][y] = True
    queue = []
    queue.append(Node(x, y))

    while len(queue) > 0:
        node = queue.pop(0)
        for i in range(4):
            newNode = Node(node.x + direX[i], node.y + direY[i])
            if not inGraph(newNode, grid) or visited[newNode.x][newNode.y] \
                    or grid[newNode.x][newNode.y] == "x":
                continue
            dp[newNode.x][newNode.y] = min(dp[newNode.x][newNode.y], grid[newNode.x][newNode.y] + dp[node.x][node.y])
            queue.append(Node(newNode.x, newNode.y))
            visited[newNode.x][newNode.y] = True

def inGraph(node, grid):
    if node.x < 0 or node.x >= len(grid):
        return False
    elif node.y < 0 or node.y >= len(grid[0]):
        return False
    else:
        return True

grid = [[1,1,1], [1,2,"x"], [0,1,1]]
print minPathSum(grid)