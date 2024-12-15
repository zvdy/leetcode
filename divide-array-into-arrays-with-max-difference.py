from typing import *
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # Sort the input list in ascending order
        nums.sort()
        
        # Initialize the result list
        ans = []
        
        # Check if the length of the list is divisible by 3
        # If not, return an empty list
        if len(nums) % 3 != 0:
            return []
        
        # Iterate over the list in steps of 3
        for i in range(0, len(nums), 3):
            # If the difference between the third and first number in the current group is greater than k
            # Return an empty list
            if nums[i + 2] - nums[i] > k:
                return []
            
            # Append the current group of 3 numbers to the result list
            ans.append([nums[i], nums[i + 1], nums[i + 2]])
        
        # Return the result list
        return ans
