class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = [[] for _ in range(n)]
        blue = [[] for _ in range(n)]
        for u, v in redEdges:
            red[u].append(v)
        for u, v in blueEdges:
            blue[u].append(v)
        q = deque([(0, 0, 0), (0, 1, 0)])
        visited = set([(0, 0), (0, 1)])
        ans = [float('inf')] * n
        ans[0] = 0
        while q:
            u, color, dist = q.popleft()
            if color == 0:
                for v in red[u]:
                    if (v, 1) not in visited:
                        visited.add((v, 1))
                        q.append((v, 1, dist + 1))
                        ans[v] = min(ans[v], dist + 1)
            else:
                for v in blue[u]:
                    if (v, 0) not in visited:
                        visited.add((v, 0))
                        q.append((v, 0, dist + 1))
                        ans[v] = min(ans[v], dist + 1)
        return [x if x != float('inf') else -1 for x in ans]