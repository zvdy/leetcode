from typing import *
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # Create a dictionary to store the frequency of each character in the words
        d = {}
        for i in words:
            for j in i:
                if j in d:
                    d[j] += 1
                else:
                    d[j] = 1

        # Iterate over the dictionary
        for i in d:
            # If the frequency of the current character is not divisible by the number of words, return False
            if d[i] % len(words) != 0:
                return False
            
        # If we have not returned False by this point, return True
        return True
    
