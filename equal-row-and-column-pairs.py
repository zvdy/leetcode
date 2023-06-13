class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hist = {}
        n = 0
        i = 0
        
        while i < len(grid):
            r = '.'.join([str(num) for num in grid[i]])
            hist[r] = hist.get(r, 0) + 1
            i += 1
        c = 0
        
        while c < len(grid):
            s = '.'.join([str(grid[r][c]) for r in range(len(grid))])
            n += hist.get(s, 0)
            c += 1

        return n