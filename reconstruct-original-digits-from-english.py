from typing import *
from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        
        digits = [
            (0, 'zero', 'z'),
            (2, 'two', 'w'),
            (4, 'four', 'u'),
            (6, 'six', 'x'),
            (8, 'eight', 'g'),
            (1, 'one', 'o'),
            (3, 'three', 'r'),
            (5, 'five', 'f'),
            (7, 'seven', 's'),
            (9, 'nine', 'i'),
        ]
        
        result = []
        
        for digit, word, char in digits:
            while count[char] > 0:
                result.append(str(digit))
                
                for c in word:
                    count[c] -= 1
        
        return ''.join(sorted(result))
    
