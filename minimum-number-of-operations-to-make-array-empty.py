from typing import *
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Create a counter object that counts the occurrence of each number in the list
        counter = Counter(nums)
        
        # Initialize the answer to 0
        ans = 0
        
        # Iterate over the values of the counter (i.e., the counts of each number)
        for c in counter.values():
            # If any number appears only once, return -1 as per the problem statement
            if c == 1: 
                return -1
            
            # Add the ceiling of the count divided by 3 to the answer
            # This is because each operation can decrease the count of a number by up to 3
            ans += ceil(c / 3)
        
        # Return the total number of operations
        return ans
