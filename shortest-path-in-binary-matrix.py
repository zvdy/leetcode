from typing import *
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        n = len(grid)
        q = [(0, 0, 1)]
        grid[0][0] = 1
        while q:
            x, y, d = q.pop(0)
            if x == n - 1 and y == n - 1: return d
            for i, j in [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                         (x, y - 1), (x, y + 1),
                         (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]:
                if 0 <= i < n and 0 <= j < n and grid[i][j] == 0:
                    q.append((i, j, d + 1))
                    grid[i][j] = 1
        return -1