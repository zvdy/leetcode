class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)  # Get the length of the input array
        if n == 1:
            return arr[0]  # If the array has only one element, return that element
        count = 1  # Initialize a counter variable to keep track of the frequency of the current element
        for i in range(1, n):
            if arr[i] == arr[i-1]:  # If the current element is the same as the previous element
                count += 1  # Increment the counter
                if count > n/4:  # If the counter exceeds 25% of the array length
                    return arr[i]  # Return the current element as it appears more than 25% of the time
            else:
                count = 1  # Reset the counter if the current element is different from the previous element
        return -1  # If no element appears more than 25% of the time, return -1