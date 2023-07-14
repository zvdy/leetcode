class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # Create a dictionary to store the length of the longest subsequence
        # that ends at each number
        dp = {}
        # Iterate through the array
        for num in arr:
            # If the previous number is in the dictionary, add one to the length
            # of the longest subsequence that ends at this number
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1
            # Otherwise, the length of the longest subsequence that ends at this
            # number is one
            else:
                dp[num] = 1
        # Return the maximum length
        return max(dp.values())