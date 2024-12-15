from typing import *
class Solution:
    def sortVowels(self, s: str) -> str:
        # Sort the vowels in descending order
        vowels_sorted = sorted([c for c in s if c.lower() in 'aeiou'], reverse=True)

        result = []
        # Iterate through each character in the string
        for char in s:
            # If the character is a vowel, append the next largest vowel from the sorted list
            if char.lower() in 'aeiou':
                result.append(vowels_sorted.pop())
            # Otherwise, append the character as is
            else:
                result.append(char)

        # Join the resulting list of characters into a string and return it
        return ''.join(result)