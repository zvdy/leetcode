from typing import *
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # Get the length of the array
        n = len(arr)
        
        # Initialize a dynamic programming (DP) array with zeros
        dp = [0] * (n + 1)
        
        # Iterate over the array
        for i in range(n):
            # Initialize the current maximum value
            curMax = 0
            
            # Iterate over the possible partition sizes (up to k)
            for j in range(1, k + 1):
                # Check if the partition is valid (i.e., it doesn't start before the array)
                if i - j + 1 >= 0:
                    # Update the current maximum value if necessary
                    curMax = max(curMax, arr[i - j + 1])
                    
                    # Update the DP value for the current position, considering the current partition
                    dp[i + 1] = max(dp[i + 1], dp[i - j + 1] + curMax * j)
        
        # Return the maximum sum after partitioning the array
        return dp[n]
