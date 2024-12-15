from typing import *
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, m+1):
            dp[1][i][1] = 1
        for i in range(2, n+1):
            for j in range(1, m+1):
                for l in range(1, k+1):
                    dp[i][j][l] = (dp[i][j][l] + dp[i-1][j][l]*j) % (10**9+7)
                    for p in range(1, j):
                        dp[i][j][l] = (dp[i][j][l] + dp[i-1][p][l-1]) % (10**9+7)
        return sum(dp[n][i][k] for i in range(1, m+1)) % (10**9+7)