from collections import defaultdict
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        G = defaultdict(list)
        for i in range(1,len(parent)):
            G[parent[i]].append(i)
        self.ans = 1
        def dfs(v):
            if not G[v]: return 1
            res = 1
            for w in G[v]:
                length_of_child = dfs(w)
                if s[v] != s[w]:
                    self.ans = max(self.ans, length_of_child+res)
                    res = max(res, length_of_child+1)
            return res
        dfs(0)
        return self.ans
