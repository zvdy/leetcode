from typing import *
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # If the target is less than the number of dice or greater than the maximum possible sum, return 0
        if target < n or target > n * k:
            return 0

        # Initialize a 2D dynamic programming table with size (n+1) x (target+1)
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # For one dice, the number of ways to get the sum i is 1 for all i in [1, min(k, target)]
        for i in range(1, min(k + 1, target + 1)):
            dp[1][i] = 1

        # For each number of dice from 2 to n
        for i in range(2, n + 1):
            # For each possible sum from 1 to target
            for j in range(1, target + 1):
                # For each possible face value from 1 to min(k, j)
                for l in range(1, min(k + 1, j)):
                    # Add the number of ways to get the sum j - l with one less dice
                    dp[i][j] += dp[i - 1][j - l]
                # Take the result modulo 1e9 + 7 to prevent overflow
                dp[i][j] %= 1000000007

        # Return the number of ways to get the target sum with n dice
        return dp[n][target]
