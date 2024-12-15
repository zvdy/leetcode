from typing import *
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        parent = [i for i in range(n)]
        def find(x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            parent[find(x)] = find(y)
        for x,y in connections:
            union(x,y)
        res = 0
        for i in range(n):
            if parent[i]==i:
                res+=1
        return res-1