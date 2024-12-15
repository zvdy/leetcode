from typing import *
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # Create a dictionary to store the frequency of each character in the words
        d = {}
        for i in words:  # Iterate over each word in the list
            for j in i:  # Iterate over each character in the current word
                if j in d:  # If the character is already in the dictionary, increment its count
                    d[j] += 1
                else:  # If the character is not in the dictionary, add it with a count of 1
                    d[j] = 1

        # Iterate over the dictionary
        for i in d:
            # If the frequency of the current character is not divisible by the number of words, return False
            # This is because if a character's frequency is not divisible by the number of words, 
            # it means we can't distribute it evenly among all words
            if d[i] % len(words) != 0:
                return False
            
        # If we have not returned False by this point, it means all characters can be evenly distributed among all words
        # So, we return True
        return True
