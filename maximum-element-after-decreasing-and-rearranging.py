from typing import *
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Sort the array in ascending order
        arr.sort()
        # Set the first element to 1
        arr[0] = 1
        # Iterate through the array starting from the second element
        for i in range(1, len(arr)):
            # If the difference between the current element and the previous element is greater than 1,
            # set the current element to the previous element plus 1
            if arr[i] - arr[i - 1] > 1:
                arr[i] = arr[i - 1] + 1
        # Return the last element in the array
        return arr[-1]