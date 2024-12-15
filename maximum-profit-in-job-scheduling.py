from typing import *
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine the start times, end times, and profits into a single list of jobs
        # Sort the jobs by their end times
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        # Initialize the dynamic programming table with a single job that starts and ends at time 0 and has profit 0
        dp = [[0, 0]]
        
        # Iterate over the jobs
        for s, e, p in jobs:
            # Find the index of the last job that ends before the current job starts
            i = bisect.bisect(dp, [s+1]) - 1
            
            # If the profit of the current job plus the profit of the last job that ends before it starts
            # is greater than the profit of the last job in the dp table
            if dp[i][1] + p > dp[-1][1]:
                # Add the current job to the dp table
                dp.append([e, dp[i][1] + p])
        
        # Return the maximum profit, which is the profit of the last job in the dp table
        return dp[-1][1]
