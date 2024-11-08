from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        xor = 0
        
        # Calculate the XOR of all elements in nums
        for num in nums:
            xor ^= num
        
        result = []
        
        # Iterate from the last index to the first
        for i in range(n - 1, -1, -1):
            # Create a mask with all bits set to 1 up to maximumBit
            mask = (1 << maximumBit) - 1
            # XOR the mask with the current xor value
            mask ^= xor
            
            # Append the result to the list
            result.append(mask)
            
            # Update the xor by removing the effect of the current element
            xor ^= nums[i]
        
        return result