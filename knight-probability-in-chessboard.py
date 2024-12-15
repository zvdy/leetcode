from typing import *
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # dp[i][j] = probability of being on the board at (i, j) after k moves
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1
        for _ in range(k):
            new_dp = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for di, dj in ((-2, -1), (-2, 1), (-1, -2), (-1, 2),
                                   (1, -2), (1, 2), (2, -1), (2, 1)):
                        if 0 <= i + di < n and 0 <= j + dj < n:
                            new_dp[i + di][j + dj] += dp[i][j] / 8
            dp = new_dp
        return sum(sum(row) for row in dp)