from typing import *
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        for i,(x1,y1,r1) in enumerate(bombs):
            for j,(x2,y2,_) in enumerate(bombs):
                if (x2-x1)**2+(y2-y1)**2 <= r1**2:
                    graph[i].append(j)

        answer = 1
        for i in range(n):
            que = deque([i])
            visited = set()
            while que:
                node = que.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for nb in graph[node]:
                    que.append(nb)
            answer = max(answer,len(visited))
        return answer