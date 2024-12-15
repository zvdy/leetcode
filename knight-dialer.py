from typing import *
class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        moves = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        dp = [1] * 10
        for _ in range(n - 1):
            dp2 = [0] * 10
            for i in range(10):
                for j in moves[i]:
                    dp2[j] += dp[i]
                    dp2[j] %= MOD
            dp = dp2
        return sum(dp) % MOD