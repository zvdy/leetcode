from typing import *
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Define a set of vowels, both lowercase and uppercase
        vowels = set('aeiouAEIOU')
        
        # The sum function counts the number of vowels in the first half of the string
        # The '1 for c in s[:len(s)//2] if c in vowels' is a generator expression that generates 1 for each vowel in the first half of the string
        # The sum of these 1's is the number of vowels in the first half of the string
        
        # Similarly, the number of vowels in the second half of the string is computed
        
        # The function returns True if the number of vowels in the first half is equal to the number of vowels in the second half, and False otherwise
        return sum(1 for c in s[:len(s)//2] if c in vowels) == sum(1 for c in s[len(s)//2:] if c in vowels)
