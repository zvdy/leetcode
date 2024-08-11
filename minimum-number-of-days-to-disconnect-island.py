from collections import deque
import copy  # Import copy for deepcopy
from typing import List  # Import List from typing for type hinting

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # Initialize dimensions and directions for traversal
        m, n = len(grid), len(grid[0])
        dirr = [1, 0, -1, 0]
        dirc = [0, 1, 0, -1]
        visreq = set()  # Set to keep track of cells to visit
        cntone = 0  # Counter for number of 1s in the grid
        
        # Count 1s and add their positions to visreq
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cntone += 1
                    visreq.add((i, j))
        
        # If there's only one 1, return 1
        if cntone == 1:
            return 1
                
        # Function to check if a position is valid
        def isvalid(i, j, m, n, gridma):
            return 0 <= i < m and 0 <= j < n and gridma[i][j] == 1
        
        # BFS function to traverse the grid
        def bfs(source, vis, gridpa):
            q = deque()
            q.append(source)
            vis.add(source)
            
            while q:
                x, y = q.popleft()
                for i in range(4):
                    adjx = dirr[i] + x
                    adjy = dirc[i] + y
                    if (adjx, adjy) not in vis and isvalid(adjx, adjy, m, n, gridpa):
                        vis.add((adjx, adjy))
                        q.append((adjx, adjy))
            return vis
        
        # Check if the grid is already disconnected
        glovis = set()  # Global visited set
        cnt = 0  # Counter for number of disconnected parts
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in glovis:
                    glovis = glovis.union(bfs((i, j), set(), grid))
                    cnt += 1
                    if glovis == visreq:
                        break
                        
        # If more than one disconnected part, return 0
        if cnt != 1:
            return 0
        
        # Check by removing each 1 if the grid becomes disconnected
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    gridcopy = copy.deepcopy(grid)  # Make a copy of the grid
                    gridcopy[i][j] = 0  # Remove a 1
                    glovis = set()  # Reset global visited set
                    visreqpa = set()  # Reset cells to visit
                    
                    # Update visreqpa for the copied grid
                    for f in range(m):
                        for e in range(n):
                            if gridcopy[f][e] == 1:
                                visreqpa.add((f, e))
                    
                    cnt = 0  # Reset counter
                    for f in range(m):
                        for e in range(n):
                            if gridcopy[f][e] == 1 and (f, e) not in glovis:
                                glovis = glovis.union(bfs((f, e), set(), gridcopy))
                                cnt += 1
                                if glovis == visreqpa and cnt != 1:
                                    return 1  # Return 1 if disconnected by removing a 1
                                
        return 2  # Return 2 if the grid is not disconnected or requires removing more than one 1