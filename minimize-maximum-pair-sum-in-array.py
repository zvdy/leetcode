from typing import *
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # Initialize the maximum pair sum to 0
        max_pair_sum = 0
        # Sort the numbers
        nums.sort()
        # For each number in the list
        for i in range(len(nums) // 2):
            # Calculate the pair sum
            pair_sum = nums[i] + nums[-(i + 1)]
            # Update the maximum pair sum
            max_pair_sum = max(max_pair_sum, pair_sum)
        # Return the maximum pair sum
        return max_pair_sum