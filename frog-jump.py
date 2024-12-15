from typing import *
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        if len(stones) == 2:
            return True
        if len(stones) == 3:
            return stones[2] == 2
        dp = [set() for _ in range(len(stones))]
        dp[1].add(1)
        for i in range(2, len(stones)):
            for j in range(1, i):
                if stones[i] - stones[j] - 1 in dp[j]:
                    dp[i].add(stones[i] - stones[j])
                if stones[i] - stones[j] in dp[j]:
                    dp[i].add(stones[i] - stones[j])
                if stones[i] - stones[j] + 1 in dp[j]:
                    dp[i].add(stones[i] - stones[j])
            if i == len(stones) - 1:
                return len(dp[i]) > 0
        return False