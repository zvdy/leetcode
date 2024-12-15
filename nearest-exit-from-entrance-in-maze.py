from typing import *
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        visited = set()
        queue = deque([(entrance[0], entrance[1], 0)])
        while queue:
            x, y, d = queue.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if d > 0 and (x == 0 or x == m - 1 or y == 0 or y == n - 1):
                return d
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    queue.append((nx, ny, d + 1))
        return -1