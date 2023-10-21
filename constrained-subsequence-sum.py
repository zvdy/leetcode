class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        q = collections.deque()
        q.append(0)
        for i in range(1, n):
            dp[i] = nums[i]
            if q[0] < i - k:
                q.popleft()
            dp[i] = max(dp[i], dp[q[0]] + nums[i])
            while q and dp[q[-1]] < dp[i]:
                q.pop()
            q.append(i)
        return max(dp)