from typing import *
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        d = {i:[1, 0] for i in range(n)}
        
        def dfs(root, prev):
            for nei in g[root]:
                if nei != prev:
                    dfs(nei, root)
                    d[root][0] += d[nei][0]
                    d[root][1] += (d[nei][0] + d[nei][1])
        
        def dfs2(root, prev):
            for nei in g[root]:
                if nei != prev:
                    d[nei][1] = d[root][1] - d[nei][0] + (n-d[nei][0])
                    dfs2(nei, root)
        
        dfs(0, -1)
        dfs2(0, -1)
        res = []
        for key in d:
            res.append(d[key][1])
        return res
        