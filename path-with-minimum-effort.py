class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        m, n = len(heights), len(heights[0])
        edges = []
        for i in range(m):
            for j in range(n):
                if i > 0:
                    edges.append((abs(heights[i][j] - heights[i - 1][j]), (i, j), (i - 1, j)))
                if j > 0:
                    edges.append((abs(heights[i][j] - heights[i][j - 1]), (i, j), (i, j - 1)))
        
        edges.sort()
        parent = list(range(m * n))
        rank = [0] * (m * n)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[px] = py
                rank[py] += 1
            return True
        
        for cost, u, v in edges:
            if union(u[0] * n + u[1], v[0] * n + v[1]):
                if find(0) == find(m * n - 1):
                    return cost
        
        return 0