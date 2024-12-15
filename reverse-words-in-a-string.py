from typing import *
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])