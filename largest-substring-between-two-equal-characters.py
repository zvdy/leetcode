from typing import *
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_len = -1  # Variable to store the maximum length between equal characters
        for i in range(len(s)):
            for j in range(len(s)):
                # Check if the characters at indices i and j are equal and i is not equal to j
                if s[i] == s[j] and i != j:
                    # Calculate the length between the equal characters and update max_len if necessary
                    max_len = max(max_len, abs(i - j) - 1)
        return max_len  # Return the maximum length between equal characters