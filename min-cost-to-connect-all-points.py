from typing import List
from collections import defaultdict
import heapq

## Kruskal's algorithm

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(points[i], points[j]), i, j))
        
        edges.sort()
        parent = list(range(n))
        rank = [0] * n
        res = 0
        
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
            if union(u, v):
                res += cost
        
        return res