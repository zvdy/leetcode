class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Start from the end of the number
        for i in range(len(num) - 1, -1, -1):
            # If the current digit is odd
            if int(num[i]) % 2 == 1:
                # Return the number up to and including the current digit
                return num[:i + 1]
        # If no odd digit is found, return an empty string
        return ""
