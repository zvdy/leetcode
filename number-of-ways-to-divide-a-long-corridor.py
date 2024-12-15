from typing import *
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # Define the modulus for the result
        MOD = 1_000_000_007

        # Initialize a cache for memoization
        cache = [[-1] * 3 for _ in range(len(corridor))]

        # Define a helper function to count the number of ways
        def count(index, seats):
            # If we have reached the end of the corridor
            if index == len(corridor):
                # If there are exactly 2 seats in the current section, return 1
                # Otherwise, return 0
                return 1 if seats == 2 else 0

            # If the result of this sub-problem is already computed, return it
            if cache[index][seats] != -1:
                return cache[index][seats]
            
            # If the current section has exactly 2 seats
            if seats == 2:
                # If the current element is "S", we must start a new section
                if corridor[index] == "S":
                    result = count(index + 1, 1)
                else:
                    # If the current element is "P", we can either start a new section
                    # or continue the current section
                    result = (count(index + 1, 0) + count(index + 1, 2)) % MOD
            else:
                # If the current section has less than 2 seats, we can continue the section
                # If the current element is "S", increment the seat count
                if corridor[index] == "S":
                    result = count(index + 1, seats + 1)
                else:
                    result = count(index + 1, seats)
            
            # Store the result in the cache
            cache[index][seats] = result
            return cache[index][seats]
        
        # Start the count from the first index with 0 seats
        return count(0, 0)
