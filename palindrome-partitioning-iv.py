class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for l in range(1, n+1):
          for i in range(n-l+1):
            j = i + l - 1
            if s[i] == s[j]:
              dp[i][j] = j-i<2 or dp[i+1][j-1]

        for i in range(n-2):
          if dp[0][i]:
            for j in range(i+1,n-1):
              if dp[i+1][j] and dp[j+1][n-1]:
                return True
        return False