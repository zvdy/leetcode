from typing import *
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                return +(j == 0)
            ans = dp(i-1, j-1) * (n-j+1)
            ans += dp(i-1, j) * max(j-k, 0)
            return ans % (10**9 + 7)
        return dp(goal, n)