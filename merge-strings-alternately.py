from typing import *
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        i = 0
        while i < len(word1) and i < len(word2):
            s += word1[i] + word2[i]
            i += 1
        if i < len(word1):
            s += word1[i:]
        if i < len(word2):
            s += word2[i:]
        return s