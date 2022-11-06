class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # 1st solution
        # O(n) time, O(n) space
        # Runtime: 1080 ms, faster than 100.00%
        # Memory Usage: 63.6 MB, less than 100.00%
        res = 0
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(-u)
        visited = set()
        def dfs(node):
            nonlocal res
            visited.add(node)
            for nei in graph[node]:
                if abs(nei) not in visited:
                    if nei > 0:
                        res += 1
                    dfs(abs(nei))
        dfs(0)
        return res