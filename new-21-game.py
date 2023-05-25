class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0
        if k == 1:
            return min(n, maxPts)/maxPts
        if maxPts == 1:
            return 1.0 if n >= k else 0.0
        dp = [0.0 for _ in range(k+maxPts)]
        dp[0] = 1.0
        for i in range(1, k+maxPts):
            dp[i] = dp[i-1]
            if i <= maxPts:
                dp[i] += dp[i-1]
            else:
                dp[i] += dp[i-1] - dp[i-1-maxPts]
            if i >= k:
                dp[i] -= dp[i-k-1]
        ans = 0.0
        for i in range(k, n+1):
            ans += dp[i]
        return ans / dp[k-1]