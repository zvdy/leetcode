from typing import *
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Initialize an empty dictionary to store the occurrences of each number
        d = {}
        # Iterate over each number in the input list
        for i in arr:
            # If the number is not already in the dictionary, add it with a count of 1
            if i not in d:
                d[i] = 1
            # If the number is already in the dictionary, increment its count
            else:
                d[i] += 1
        
        # Return True if the number of unique counts is equal to the total number of counts
        # This means that each number has a unique count
        return len(d.values()) == len(set(d.values()))
