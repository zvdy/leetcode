from typing import *
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Sort the input list
        nums.sort()
        
        # Initialize left and right pointers, total sum and answer
        l, r, total, ans = 0, 0, 0, 1
        
        # Iterate over the list
        while r < len(nums):
            # Add the current number to the total sum
            total += nums[r]
            
            # If the difference between the total sum and the product of the current number and the range is greater than k
            # Move the left pointer to the right and subtract the number at the left pointer from the total sum
            while (r - l + 1) * nums[r] - total > k:
                total -= nums[l]
                l += 1
            
            # Update the answer with the maximum frequency
            ans = max(ans, r - l + 1)
            
            # Move the right pointer to the right
            r += 1
        
        # Return the maximum frequency
        return ans