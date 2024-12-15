from typing import *
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # Get the length of the input list
        n = len(nums)
        
        # If the list has less than 3 elements, return 0 as no arithmetic slice can be formed
        if n < 3:
            return 0
        
        # Initialize a list of defaultdicts for dynamic programming
        dp = [defaultdict(int) for _ in range(n)]
        
        # Initialize the result to 0
        res = 0
        
        # Iterate over the list
        for i in range(n):
            # For each element, iterate over all previous elements
            for j in range(i):
                # Calculate the difference between the current and the previous element
                diff = nums[i] - nums[j]
                
                # Increment the count of this difference in the dp table for the current element
                dp[i][diff] += 1
                
                # If this difference exists in the dp table for the previous element
                if diff in dp[j]:
                    # Add the count of this difference from the dp table of the previous element
                    # to the dp table of the current element
                    dp[i][diff] += dp[j][diff]
                    
                    # Add the count of this difference from the dp table of the previous element to the result
                    res += dp[j][diff]
        
        # Return the result
        return res
