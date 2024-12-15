from typing import *
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Create a set of the input array
        nums_set = set(nums)
        # Iterate through all possible binary strings of length n
        for i in range(2 ** len(nums)):
            # Convert the integer to a binary string
            binary_string = bin(i)[2:]
            # Pad the binary string with leading zeros
            binary_string = '0' * (len(nums) - len(binary_string)) + binary_string
            # If the binary string is not in the set, return it
            if binary_string not in nums_set:
                return binary_string