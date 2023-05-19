class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                q = deque([i])
                while q:
                    node = q.popleft()
                    for nei in graph[node]:
                        if nei not in color:
                            color[nei] = color[node] ^ 1
                            q.append(nei)
                        elif color[nei] == color[node]:
                            return False
        return True