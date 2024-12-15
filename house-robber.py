from typing import *
class Solution:
    def rob(self, nums: List[int]) -> int:
        # If there's only one house, the maximum amount of money we can rob is the money in that house
        if len(nums) == 1:
            return nums[0]
        
        # If there are two houses, the maximum amount of money we can rob is the maximum of the money in the two houses
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # Initialize a list to store the maximum amount of money we can rob from the first i houses
        dp = [0] * len(nums)
        dp[0] = nums[0]  # The maximum amount of money we can rob from the first house is the money in the first house
        dp[1] = max(nums[1], nums[0])  # The maximum amount of money we can rob from the first two houses is the maximum of the money in the two houses
        
        # For each house from the third one, the maximum amount of money we can rob is the maximum of:
        # 1. The maximum amount of money we can rob from the previous house
        # 2. The money in the current house plus the maximum amount of money we can rob from the house two places before
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        # Return the maximum amount of money we can rob from all the houses
        return dp[-1]
