from typing import *
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return []
        if not wordDict:
            return []
        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = [""]
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    for word in dp[j]:
                        dp[i].append(word + " " + s[j:i] if word else s[j:i])
        return dp[-1]