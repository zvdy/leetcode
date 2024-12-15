from typing import *
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Create a dictionary to store the frequency of each character in the input string
        freq = {}
        
        # Iterate over the input string and populate the dictionary
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        # Iterate over the input string again to find the first unique character
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        
        # If no unique character is found, return -1
        return -1
