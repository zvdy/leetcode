class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find_parent(self, p):
        if self.parent[p] == p:
            return p
        self.parent[p] = self.find_parent(self.parent[p])
        return self.parent[p]
    
    def union(self, u, v):
        pu, pv = self.find_parent(u), self.find_parent(v)
        self.parent[pu] = pv

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def cmp(a, b):
            return a[2] < b[2]
        
        critical, pseudo_critical = [], []
        
        for i in range(len(edges)):
            edges[i].append(i)
        
        edges.sort(key=lambda x: x[2])
        
        mst_wt = self.find_mst(n, edges, -1, -1)
        
        for i in range(len(edges)):
            if mst_wt < self.find_mst(n, edges, i, -1):
                critical.append(edges[i][3])
            elif mst_wt == self.find_mst(n, edges, -1, i):
                pseudo_critical.append(edges[i][3])
        
        return [critical, pseudo_critical]
    
    def find_mst(self, n, edges, block, e):
        uf = UnionFind(n)
        weight = 0
        
        if e != -1:
            weight += edges[e][2]
            uf.union(edges[e][0], edges[e][1])
        
        for i in range(len(edges)):
            if i == block:
                continue
            if uf.find_parent(edges[i][0]) == uf.find_parent(edges[i][1]):
                continue
            uf.union(edges[i][0], edges[i][1])
            weight += edges[i][2]
        
        for i in range(n):
            if uf.find_parent(i) != uf.find_parent(0):
                return float('inf')
        
        return weight