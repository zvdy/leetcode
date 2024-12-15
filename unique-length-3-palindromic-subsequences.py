from typing import *
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Create a set of unique letters in the string
        letters = set(s)
        # Initialize a variable to store the answer
        ans = 0
        
        # Iterate through each unique letter in the string
        for letter in letters:
            # Find the first and last occurrences of the current letter in the string
            i, j = s.index(letter), s.rindex(letter)
            # Initialize a set to store the characters between the first and last occurrences of the current letter
            between = set()
            
            # Iterate through the characters between the first and last occurrences of the current letter
            for k in range(i + 1, j):
                # Add the current character to the set
                between.add(s[k])
            
            # Add the length of the set to the answer variable
            ans += len(between)

        # Return the answer
        return ans