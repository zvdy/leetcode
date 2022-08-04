class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
# Use dynamic programming to solve this problem.
# Use Deepth-First Search to solve this problem.

        if m == n == 1:
            return 1
        dp = [[1]*m]*n
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]