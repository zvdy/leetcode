class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # DP
        # Time: O(mn)
        # Space: O(mn)
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0]:
            return 0
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1
        for j in range(1, n):
            if obstacleGrid[0][j]:
                break
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]