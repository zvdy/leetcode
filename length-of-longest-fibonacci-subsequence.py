from typing import *
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[2] * n for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                k = bisect.bisect_left(arr, arr[i] + arr[j])
                if k < n and arr[k] == arr[i] + arr[j]:
                    dp[j][k] = dp[i][j] + 1
                    ans = max(ans, dp[j][k])
        return ans if ans >= 3 else 0