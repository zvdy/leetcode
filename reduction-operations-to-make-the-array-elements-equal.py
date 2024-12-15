from typing import *
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # Sort the input list
        nums.sort()
        
        # Initialize the answer and the variable to keep track of the number of unique elements
        ans = 0
        up = 0
        
        # Iterate over the list starting from the second element
        for i in range(1, len(nums)):
            # If the current element is not equal to the previous one, increment the number of unique elements
            if nums[i] != nums[i - 1]:
                up += 1
                
            # Add the number of unique elements to the answer
            ans += up
        
        # Return the answer
        return ans