from typing import *
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        dp = [0] * (len(s) + 1)  # Initialize a dynamic programming array to store the number of decodings
        
        dp[0] = 1  # There is only one way to decode an empty string
        dp[1] = 1  # There is only one way to decode a string of length 1
        
        for i in range(2, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]  # If the current digit is not zero, it can be decoded individually
            
            if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] < '7'):
                dp[i] += dp[i - 2]  # If the current digit and the previous digit form a valid two-digit number, it can be decoded together
        
        return dp[len(s)]  # Return the number of decodings for the entire string