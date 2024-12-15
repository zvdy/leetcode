from typing import *
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')