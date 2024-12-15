from typing import *
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        q = deque([(0, '')])
        while q:
            pos, perm = q.pop()
            if pos == len(s):
                res.append(perm)
            else:
                if s[pos].isalpha():
                    q.append((pos + 1, perm + s[pos].lower()))
                    q.append((pos + 1, perm + s[pos].upper()))
                else:
                    q.append((pos + 1, perm + s[pos]))
        return res