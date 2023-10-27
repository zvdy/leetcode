class Solution:
    def longestPalindrome(self, s: str) -> str:
        # If the string is empty, return an empty string
        if not s:
            return ''
        # If the string has only one character, return the string
        if len(s) == 1:
            return s
        # If the string has only two characters, return the first character if they are different, or the whole string if they are the same
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        # Initialize variables to keep track of the longest palindrome found so far
        max_len = 1
        start = 0
        # Iterate through the string
        for i in range(len(s)):
            # Check if the substring s[i-max_len-1:i+1] is a palindrome
            if i - max_len >= 1 and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]:
                # If it is, update the start index and the length of the longest palindrome found so far
                start = i - max_len - 1
                max_len += 2
                continue
            # Check if the substring s[i-max_len:i+1] is a palindrome
            if i - max_len >= 0 and s[i - max_len:i + 1] == s[i - max_len:i + 1][::-1]:
                # If it is, update the start index and the length of the longest palindrome found so far
                start = i - max_len
                max_len += 1
        # Return the longest palindrome found
        return s[start:start + max_len]