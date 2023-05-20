class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
            
            graph = collections.defaultdict(dict)
            
            for (x, y), val in zip(equations, values):
                graph[x][y] = val
                graph[y][x] = 1 / val
                
            def dfs(x, y, visited):
                if x not in graph or y not in graph:
                    return -1.0
                if y in graph[x]:
                    return graph[x][y]
                
                for i in graph[x]:
                    if i not in visited:
                        visited.add(i)
                        temp = dfs(i, y, visited)
                        if temp != -1.0:
                            return graph[x][i] * temp
                return -1.0
            
            res = []
            for x, y in queries:
                visited = set()
                res.append(dfs(x, y, visited))
            return res