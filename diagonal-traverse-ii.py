from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # Initialize an empty list to store the diagonal elements
        result = [] 
        
        # Iterate over each row in the input list
        for i, row in enumerate(nums):  
            # Iterate over each element in the row
            for j, num in enumerate(row):  
                # If the current diagonal doesn't exist in the result list
                if len(result) <= i + j:  
                    # Add a new empty list to represent the diagonal
                    result.append([])  
                # Add the current element to the corresponding diagonal list
                result[i + j].append(num)  
        
        # Flatten the diagonal lists and return the result
        return [num for row in result for num in reversed(row)]  