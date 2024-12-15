from typing import *
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # Define a helper function to reverse a number
        def rev(n):
            # Convert the number to a string, reverse it and convert it back to an integer
            return int(str(n)[::-1])
        
        # Initialize a Counter
        d = collections.Counter()
        
        # Iterate over the list of numbers
        for n in nums:
            # Subtract the reversed number from the original number and increment the count in the Counter
            d[n - rev(n)] += 1
        
        # Return the sum of the counts of the pairs modulo 10^9 + 7
        return sum(v * (v - 1) // 2 for v in d.values()) % (10 ** 9 + 7)