from typing import *
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
            
            # Create a graph
            graph = defaultdict(list)
            for i in range(n):
                if manager[i] != -1:
                    graph[manager[i]].append(i)
            
            # DFS
            def dfs(node, time):
                if not graph[node]:
                    return time
                else:
                    return max(dfs(child, time + informTime[node]) for child in graph[node])
            
            return dfs(headID, 0)