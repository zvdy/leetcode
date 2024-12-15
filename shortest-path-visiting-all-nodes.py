from typing import *
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = collections.deque((1 << x, x) for x in range(n))
        dist = [[float('inf')] * n for _ in range(1 << n)]
        for x in range(n):
            dist[1 << x][x] = 0

        while q:
            cover, head = q.popleft()
            d = dist[cover][head]
            if cover == (1 << n) - 1:
                return d
            for child in graph[head]:
                cover2 = cover | (1 << child)
                if d + 1 < dist[cover2][child]:
                    dist[cover2][child] = d + 1
                    q.append((cover2, child))
        return -1