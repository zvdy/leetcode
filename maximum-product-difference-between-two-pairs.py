from typing import *
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # Sort the array.
        nums.sort()
        # Return the product of the last two elements minus the product of the first two elements.
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])
