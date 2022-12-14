class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
 
        if not matrix:
            return 0
        if len(matrix) == 1:
            return min(matrix[0])
        if len(matrix) == 2:
            return min(matrix[0]) + min(matrix[1])
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        dp[0] = matrix[0]
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
                elif j == len(matrix[0]) - 1:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) + matrix[i][j]
        return min(dp[-1])