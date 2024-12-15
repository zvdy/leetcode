from typing import *
from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        x,y= -1,-1
        m,n = len(grid),len(grid[0])
        max_len = -1
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c=='@':
                    x,y = i,j
                if 'a' <= c <= 'f':
                    max_len = max(ord(c) - ord('a') + 1, max_len)
        start = [0,x,y]
        q = deque()
        visited = set()
        visited.add(f"{0} {x} {y}")
        q.append(start)
        step = 0
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                if curr[0] == (1<< max_len) - 1:
                    return step
                for d in directions:
                    i = curr[1] + d[0]
                    j = curr[2] + d[1]
                    keys = curr[0]
                    if 0<= i < m and 0<= j < n:
                        c = grid[i][j]
                        if c=='#':
                            continue
                        if 'a'<= c<= 'f':
                            keys |= 1<<(ord(c) - ord('a'))
                        if 'A' <= c<= 'F'and ((keys >> (ord(c) - ord('A'))) & 1) == 0:
                            continue
                        if f"{keys} {i} {j}" not in visited:
                            visited.add(f"{keys} {i} {j}")
                            q.append([keys, i, j])
            step += 1
        return -1
            
