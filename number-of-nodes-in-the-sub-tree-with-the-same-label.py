from typing import *
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        res = [0] * n
        def dfs(node, parent):
            count = collections.Counter()
            for child in graph[node]:
                if child != parent:
                    count += dfs(child, node)
            count[labels[node]] += 1
            res[node] = count[labels[node]]
            return count
        dfs(0, None)
        return res