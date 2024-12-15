from typing import *
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for t in range(j, target + 1):
                    dp[i][t] += dp[i - 1][t - j]
        return dp[n][target] % (10 ** 9 + 7)