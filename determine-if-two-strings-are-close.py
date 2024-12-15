from typing import *
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # If the lengths of the two words are not equal, they can't be close strings
        if len(word1) != len(word2): return False

        # Count the occurrences of each character in the two words
        c1, c2 = Counter(word1), Counter(word2)

        # Two strings are close if they have the same characters (regardless of order)
        # and the same frequencies of characters (also regardless of order)
        return sorted(c1.keys()) == sorted(c2.keys()) and sorted(c1.values()) == sorted(c2.values())
