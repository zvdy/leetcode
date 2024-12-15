from typing import *
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        if not words:
            return 0
        if not s:
            return 0
        s_map = {}
        for i in range(len(s)):
            if s[i] not in s_map:
                s_map[s[i]] = []
            s_map[s[i]].append(i)
        count = 0
        for word in words:
            if not word:
                continue
            i = 0
            prev = -1
            while i < len(word):
                if word[i] not in s_map:
                    break
                j = bisect.bisect_left(s_map[word[i]], prev + 1)
                if j == len(s_map[word[i]]):
                    break
                prev = s_map[word[i]][j]
                i += 1
            if i == len(word):
                count += 1
        return count