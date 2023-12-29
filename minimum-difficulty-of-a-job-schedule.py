class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # Get the number of jobs
        n = len(jobDifficulty)

        # If the number of jobs is less than the number of days, return -1
        if n < d:
            return -1

        # Initialize a 2D dynamic programming table with size (d) x (n) and fill it with infinity
        dp = [[float('inf')] * n for _ in range(d)]

        # The difficulty of the first job on the first day is its own difficulty
        dp[0][0] = jobDifficulty[0]

        # For each job from the second to the last
        for i in range(1, n):
            # The difficulty of the job on the first day is the maximum difficulty of all jobs so far
            dp[0][i] = max(dp[0][i - 1], jobDifficulty[i])

        # For each day from the second to the last
        for i in range(1, d):
            # For each job from the current day to the last
            for j in range(i, n):
                # Initialize the maximum difficulty of the day with the difficulty of the current job
                maxd = jobDifficulty[j]

                # For each job from the current to the first of the day
                for k in range(j, i - 1, -1):
                    # Update the maximum difficulty of the day
                    maxd = max(maxd, jobDifficulty[k])

                    # Update the minimum difficulty of the schedule ending with the current job on the current day
                    dp[i][j] = min(dp[i][j], dp[i - 1][k - 1] + maxd)

        # Return the minimum difficulty of the schedule
        return dp[-1][-1]
