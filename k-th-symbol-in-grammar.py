from typing import *
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # If n is 1, return 0
        if n == 1:
            return 0
        
        # If k is even, return 1 if the k/2-th symbol in the (n-1)-th row is 0, otherwise return 0
        if k % 2 == 0:
            return 1 if self.kthGrammar(n-1, k//2) == 0 else 0
        
        # If k is odd, return 0 if the (k+1)/2-th symbol in the (n-1)-th row is 0, otherwise return 1
        else:
            return 0 if self.kthGrammar(n-1, (k+1)//2) == 0 else 1