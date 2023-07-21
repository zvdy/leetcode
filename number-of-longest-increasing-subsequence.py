class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dp[i] = (length of LIS ending at i, number of LIS ending at i)
        dp = [(1, 1)] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i][0] < dp[j][0] + 1:
                        dp[i] = (dp[j][0] + 1, dp[j][1])
                    elif dp[i][0] == dp[j][0] + 1:
                        dp[i] = (dp[i][0], dp[i][1] + dp[j][1])
        max_len = max(dp[i][0] for i in range(len(nums)))
        return sum(dp[i][1] for i in range(len(nums)) if dp[i][0] == max_len)