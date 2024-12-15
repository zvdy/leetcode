from typing import *
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        dp = dict()
        l = len(words[0])
        m = len(target)
        n = len(words)
        count = [[0] * 26 for _ in range(l)]
        for i in range(l):
            for word in words:
                count[i][ord(word[i]) - 97] += 1
        @cache
        def solve(j, k):
            if(k == m):
                return 1
            if(j == l or m-k > l-j):
                return 0
            if((j, k) in dp):
                return dp[(j, k)]
            dp[(j, k)] = solve(j+1, k+1)*count[j][ord(target[k])-97] + solve(j+1, k)
            return dp[(j, k)]
        return solve(0, 0) % 1000000007
