from typing import *
class Solution:
    def findComplement(self, num: int) -> int:
        """
        A complement of an int is the int you get when you flip the bits of the int
        For example, the complement of 5 (101) is 2 (010)
        Return the complement of the given int
        """

        # Find the maximum number of bits
        max_bits = num.bit_length()
        # Convert num to a binary string
        num = bin(num)[2:].zfill(max_bits)
        # Find the complement of num
        complement = ''
        for i in range(max_bits):
            if num[i] == '0':
                complement += '1'
            else:
                complement += '0'
        return int(complement, 2)