from typing import *
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[j + 1] = max(dp[j + 1], dp[j] + satisfaction[i] * (j - i + 1))
        return dp[-1]