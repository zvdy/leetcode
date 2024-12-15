from typing import *
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # Sort the array in ascending order
        arr.sort()
        # Create a dictionary to store the number of binary trees for each number in the array
        dp = {}
        # Iterate over the array
        for i in range(len(arr)):
            # Initialize the number of binary trees for the current number to 1
            dp[arr[i]] = 1
            # Iterate over the previous numbers in the array
            for j in range(i):
                # If the current number is divisible by a previous number and the quotient is also in the dictionary
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in dp:
                    # Add the product of the number of binary trees for the previous number and the quotient to the current number's count
                    dp[arr[i]] += dp[arr[j]] * dp[arr[i] // arr[j]]
        # Return the sum of the number of binary trees for all numbers in the array
        return sum(dp.values()) % (10 ** 9 + 7)