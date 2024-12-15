from typing import *
class uf:
    def __init__(self,n):
        self.rank = [0 for i in range(n)]
        self.parent = [i for i in range(n)]
        
    def union(self,a,b):
        a_rep = self.find(a)
        b_rep = self.find(b)
        if a_rep != b_rep:
            rank_a_rep = self.rank[a_rep]
            rank_b_rep = self.rank[b_rep]
            if rank_a_rep < rank_b_rep :
                self.parent[a_rep] = b_rep
            elif rank_b_rep < rank_a_rep :
                self.parent[b_rep] = a_rep
            else :
                self.parent[b_rep] = a_rep
                self.rank[a_rep] += 1
    
    def find(self,a):
        if a == self.parent[a]:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def are_connected ( self,a,b):
        return self.find(a) == self.find(b)
    
            
        
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = uf(n)
        m,k = len(queries),len(edgeList)
        queries_with_index = [(i,*queries[i]) for i in range(m)]
        queries_with_index.sort(key = lambda x: x[3])
        edgeList.sort(key = lambda x:x[2])
        res = [None]*m
        
        it = 0
        for i,s,d,limit in queries_with_index:
            while it < k and edgeList[it][2]<limit:
                n1,n2,dist = edgeList[it]
                graph.union(n1,n2)
                it += 1
            res[i] = graph.are_connected(s,d)
        
        return res