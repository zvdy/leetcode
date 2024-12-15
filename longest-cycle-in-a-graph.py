from typing import *
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n
        max = -1
        for i in range(n):
            if visited[i]:
                continue
            if edges[i] == -1:
                visited[i] = True
                continue
            route = set()
            cur = i
            while edges[cur] != -1:
                visited[cur] = True
                route.add(cur)
                cur = edges[cur]
                if visited[cur] and cur not in route:
                    break
                if cur in route:
                    start = cur
                    count = 1
                    cur = edges[cur]
                    while cur != start:
                        count += 1
                        cur = edges[cur]
                    if count > max:
                        max = count
                    break
        return max
                    
