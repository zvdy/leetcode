from typing import *
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path):
            if node == len(graph) - 1:
                res.append(path)
                return
            for nei in graph[node]:
                dfs(nei, path + [nei])
        res = []
        dfs(0, [0])
        return res