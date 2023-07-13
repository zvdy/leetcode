class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create graph
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # Create visited array
        visited = [0 for _ in range(numCourses)]
        
        # DFS
        def dfs(course):
            # If we have visited this node before, we have a cycle
            if visited[course] == -1:
                return False
            # If we have visited this node before, we are done
            if visited[course] == 1:
                return True
            # Mark as visited
            visited[course] = -1
            # Visit all neighbors
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            # Mark as done
            visited[course] = 1
            return True
        
        # Visit all nodes
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True