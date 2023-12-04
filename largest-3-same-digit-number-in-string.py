class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # Create a list of all 3-digit numbers in the string that have all the same digits
        same_digit_numbers = [num[i:i+3] for i in range(len(num) - 2) if num[i] == num[i+1] == num[i+2]]
        
        # If the list is not empty, return the maximum number in the list
        # Otherwise, return an empty string
        return max(same_digit_numbers) if same_digit_numbers else ""
