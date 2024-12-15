from typing import *
class Solution:

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)



        def dfs(node):

            if node in path:
                return float("inf")
            if node in visit:
                return 0


            visit.add(node)

            path.add(node)

            color_idx = ord(colors[node]) - ord('a')

            count[node][color_idx] = 1



            for nei in adj[node]:
                if dfs(nei) == float("inf"):
                    return float("inf")
                for c in range(26):
                    count[node][c] = max(
                        count[node][c], (1 if c == color_idx else 0) + count[nei][c])

            path.remove(node)
            return max(count[node])
        n, res = len(colors), 0
        visit, path = set(), set()
        count = [[0] * 26 for _ in range(n)] 
        for i in range(n):
            res = max(dfs(i), res)
        return res if res != float("inf") else -1