from typing import *
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Define a recursive function to find the maximum length of a concatenation of unique strings
        def dfs(arr, i, s):
            # If we've reached the end of the array, return the length of the current concatenation
            if i == len(arr):
                return len(s)
            # If the current string can be added to the concatenation without repeating characters
            if len(set(s + arr[i])) == len(s) + len(arr[i]):
                # Return the maximum length we can get by either adding the current string or skipping it
                return max(dfs(arr, i + 1, s + arr[i]), dfs(arr, i + 1, s))
            else:
                # If the current string can't be added to the concatenation, skip it
                return dfs(arr, i + 1, s)
        # Start the recursion with an empty concatenation
        return dfs(arr, 0, '')
