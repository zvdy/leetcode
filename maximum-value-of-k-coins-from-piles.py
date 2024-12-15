from typing import *
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        sums = self.calc_sums(piles)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for p in range(min(j, len(piles[i - 1])) + 1):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - p] + sums[i - 1][p])
        return dp[n][k]
    
    def calc_sums(self, a):
        sums = []
        for i in range(len(a)):
            sums.append([0] * (len(a[i]) + 1))
        for i in range(len(a)):
            for j in range(1, len(a[i]) + 1):
                sums[i][j] = sums[i][j - 1] + a[i][j - 1]
        return sums