# Import List from typing module
from typing import List

class Solution:
    # Define a method that generates all sequential digits between low and high
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # Initialize an empty list to store the sequential digits
        ans = []
        
        # Iterate over the digits from 1 to 9
        for i in range(1, 9):
            # Start the sequence with the current digit
            num = i
            
            # Iterate over the remaining digits
            for j in range(i + 1, 10):
                # Append the current digit to the sequence
                num = num * 10 + j
                
                # If the sequence is within the range [low, high], add it to the list
                if low <= num <= high:
                    ans.append(num)
        
        # Sort the list in ascending order and return it
        return sorted(ans)
