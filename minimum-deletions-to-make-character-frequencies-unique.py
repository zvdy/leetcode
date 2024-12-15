from typing import *
class Solution:
    def minDeletions(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
        res = 0
        seen = set()
        for key in d:
            while d[key] in seen:
                d[key] -= 1
                res += 1
            if d[key] != 0:
                seen.add(d[key])
        return res