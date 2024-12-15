from typing import *
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        n = len(isConnected)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    adj[i].append(j)
        visited = set()
        res = 0
        
        def bfs(i):
            nonlocal res
            q = deque([i])
            visited.add(i)
            while q:
               node = q.popleft()
               for nei in adj[node]:
                   if nei not in visited:
                       visited.add(nei)
                       q.append(nei)
            
            res += 1            
            
        for i in range(n):
            if i not in visited:
                bfs(i)
            
        return res   