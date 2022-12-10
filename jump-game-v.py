class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            dp[i] = 1
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], dfs(j) + 1)
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], dfs(j) + 1)
            return dp[i]
        dp = [-1] * n
        return max(dfs(i) for i in range(n))