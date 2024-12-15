from typing import *
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        j = 0
        for c in s:
            i = t.find(c, j)
            if i == -1:
                return False
            j = i + 1
        return True