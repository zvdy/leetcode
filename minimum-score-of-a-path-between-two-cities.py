from typing import *
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        paths = defaultdict(list) 
        for x,y,l in roads:
            paths[x].append((y,l))
            paths[y].append((x,l))
        visited = set()
        
        mini = 10**10
        
        q = []
        q.append((1,10**10))
        
        while q:
            cur, l = q.pop()
            mini = min(mini,l) 
            
            if cur in visited:
                continue

            for nxt in paths[cur]:
                q.append(nxt)
            visited.add(cur)

        return mini