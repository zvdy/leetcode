from typing import *
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, len(graph[i])+len(graph[j])-(j in graph[i]))
        return ans