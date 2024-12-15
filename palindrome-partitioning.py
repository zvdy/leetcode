from typing import *
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            return s == s[::-1]
        
        def dfs(s, path, res):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s) + 1):
                if isPalindrome(s[:i]):
                    dfs(s[i:], path + [s[:i]], res)
        
        res = []
        dfs(s, [], res)
        return res