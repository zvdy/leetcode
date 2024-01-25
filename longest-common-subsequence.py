class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        
        # Create a 2D dynamic programming table with dimensions (len(text1) + 1) x (len(text2) + 1)
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        # Iterate over the rows of the table
        for i in range(1, len(text1) + 1):
            # Iterate over the columns of the table
            for j in range(1, len(text2) + 1):
                # If the characters at the current positions in text1 and text2 are equal,
                # update the value in the table by adding 1 to the diagonal element
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                # If the characters are not equal, take the maximum of the element above and the element to the left
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Return the value in the bottom-right corner of the table, which represents the length of the longest common subsequence
        return dp[-1][-1]