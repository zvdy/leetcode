class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # Define the modulus to avoid overflow
        MOD = 1000000007
        # Initialize a list with dimensions (k+1) filled with zeros
        dp = [0] * (k + 1)
        # There's only one way to arrange 0 numbers with 0 inverse pairs: an empty arrangement
        dp[0] = 1
        # Iterate over each number from 2 to n (inclusive)
        for i in range(2, n + 1):
            # Iterate over each number from 1 to k (inclusive)
            for j in range(1, k + 1):
                # Add the number of arrangements for the previous number with j-1 inverse pairs
                dp[j] = (dp[j] + dp[j - 1]) % MOD
            # Iterate over each number from k to i-1 (inclusive) in reverse order
            for j in range(k, i - 1, -1):
                # Subtract the number of arrangements for the previous number with j-i inverse pairs
                dp[j] = (dp[j] - dp[j - i] + MOD) % MOD
        # Return the number of arrangements for n with k inverse pairs
        return dp[k]
