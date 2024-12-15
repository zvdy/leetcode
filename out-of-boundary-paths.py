from typing import *
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # Define a recursive function to calculate the number of out-of-boundary paths
        @lru_cache(None)
        def dfs(i, j, k):
            # Base case: if the current position is out of the boundary, return 1
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            # Base case: if the maximum number of moves is reached, return 0
            if k == 0:
                return 0
            # Recursive case: calculate the number of paths by moving in all four directions
            return dfs(i - 1, j, k - 1) + dfs(i + 1, j, k - 1) + dfs(i, j - 1, k - 1) + dfs(i, j + 1, k - 1)
        
        # Return the number of out-of-boundary paths modulo (10^9 + 7)
        return dfs(startRow, startColumn, maxMove) % (10**9 + 7)