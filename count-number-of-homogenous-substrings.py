from typing import *
class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        prev = None
        count = 0
        # Loop through each character in the string
        for c in s:
            # If the current character is the same as the previous character, increment the count
            if c == prev:
                count += 1
            # If the current character is different from the previous character, reset the count to 1 and update the previous character
            else:
                count = 1
                prev = c
            # Add the current count to the answer
            ans += count
        # Return the answer modulo 10^9 + 7
        return ans % (10 ** 9 + 7)