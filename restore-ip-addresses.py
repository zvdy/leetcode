from typing import *
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(s, path, res):
            if not s and len(path) == 4:
                res.append('.'.join(path))
                return
            if len(path) == 4:
                return
            for i in range(1, 4):
                if i <= len(s):
                    if i == 1:
                        dfs(s[i:], path + [s[:i]], res)
                    elif i == 2 and s[0] != '0':
                        dfs(s[i:], path + [s[:i]], res)
                    elif i == 3 and s[0] != '0' and int(s[:3]) <= 255:
                        dfs(s[i:], path + [s[:i]], res)
        
        res = []
        dfs(s, [], res)
        return res