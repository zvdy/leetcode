from typing import *
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # If k is greater than or equal to the length of the array, the maximum element is the winner
        if k >= len(arr):
            return max(arr)
        
        count = 0
        # Keep looping until we have a winner
        while count < k:
            # If the first element is greater than the second element, move the second element to the end of the array
            if arr[0] > arr[1]:
                count += 1
                arr.append(arr[1])
                arr.pop(1)
            # If the second element is greater than or equal to the first element, move the first element to the end of the array
            else:
                count = 1
                arr.append(arr[0])
                arr.pop(0)
        
        # Return the first element of the array, which is the winner
        return arr[0]