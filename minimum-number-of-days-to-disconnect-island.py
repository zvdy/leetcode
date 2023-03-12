from collections import defaultdict
from collections import deque

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dirr=[1,0,-1,0]
        dirc=[0,1,0,-1]
        visreq=set()
        cntone=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    cntone+=1
                    
                    visreq.add((i,j))
                    
        if cntone==1:
            return 1
                
        def isvalid(i,j,m,n,visreq,gridma):
            if i<0 or i>m-1 or j<0 or j>n-1 or gridma[i][j]==0 :
                return False
            return True
        
        def bfs(source,vis,gridpa,visreqpa):
            q=deque()
            q.append(source)
            
            vis.add(source)
            
            while(q):
                x,y=q.popleft()
                
            
                for i in range(4):
                    adjx=dirr[i]+x
                    adjy=dirc[i]+y
                    
                    if (adjx,adjy) not in vis and isvalid(adjx,adjy,m,n,visreqpa,gridpa):
                        vis.add((adjx,adjy))
                        q.append((adjx,adjy))
                        
            return vis
        glovis=set()         
        cnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in glovis:
                    glovis=glovis.union(bfs((i,j),set(),grid,visreq))
                    cnt+=1
                    if glovis==visreq:
                        break
                        
                        
        if cnt!=1:
            return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:

                    
                    
                    gridcopy=copy.deepcopy(grid)
                    gridcopy[i][j]=0
                    glovis=set()    
                    visreqpa=set()
                    for f in range(m):
                        for e in range(n):
                            if gridcopy[f][e]==1:
                                
                                visreqpa.add((f,e))
                    
                    
                    cnt=0
                    for f in range(m):
                        for e in range(n):
                            if gridcopy[f][e]==1 and (f,e) not in glovis:
                                glovis=glovis.union(bfs((f,e),set(),gridcopy,visreqpa))
                                
                                cnt+=1
                                if glovis==visreqpa and cnt!=1:
                                    return 1
                                
        return 2