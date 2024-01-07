class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize the length of the longest increasing subsequence to 0.
        longest = 0
        # Initialize a list to store the length of the longest increasing subsequence ending at each index.
        dp = [0] * len(nums)
        # Iterate over the array.
        for i in range(len(nums)):
            # Initialize the length of the longest increasing subsequence ending at the current index to 1.
            dp[i] = 1
            # Iterate over the previous elements in the array.
            for j in range(i):
                # If the current element is greater than the previous element and the length of the longest increasing subsequence ending at the previous element plus 1 is greater than the length of the longest increasing subsequence ending at the current element, update the length of the longest increasing subsequence ending at the current element.
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
            # Update the length of the longest increasing subsequence.
            longest = max(longest, dp[i])
        # Return the length of the longest increasing subsequence.
        return longest
