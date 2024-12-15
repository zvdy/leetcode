from typing import *
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        m = len(group)
        dp = [[[0 for _ in range(m + 1)] for _ in range(minProfit + 1)] for _ in range(n + 1)]
        dp[0][0][0] = 1

        for crime in range(1, m + 1):
            for members in range(n + 1):
                for profitVal in range(minProfit + 1):
                    dp[members][profitVal][crime] = dp[members][profitVal][crime - 1]
                    if members >= group[crime - 1]:
                        remainingProfit = max(0, profitVal - profit[crime - 1])
                        dp[members][profitVal][crime] += dp[members - group[crime - 1]][remainingProfit][crime - 1]
                    dp[members][profitVal][crime] %= MOD

        totalSchemes = 0
        for members in range(n + 1):
            totalSchemes += dp[members][minProfit][m]
            totalSchemes %= MOD

        return totalSchemes

