class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        count = collections.Counter(s)
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1