class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # The idea is to use DFS to find all the connected components.
        # For each connected component, we can remove all but one stone.
        # The number of stones removed is the size of the connected component minus 1.
        # The total number of stones removed is the sum of the number of stones removed for each connected component.
        # Time complexity: O(n^2)
        # Space complexity: O(n)
        n = len(stones)
        # Create a graph with n nodes, where each node represents a stone.
        # Two stones are connected if they share the same row or column.
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)
        # Use DFS to find all the connected components.
        visited = [False] * n
        def dfs(i):
            if visited[i]:
                return 0
            visited[i] = True
            return 1 + sum(dfs(j) for j in graph[i])
        return sum(dfs(i) - 1 for i in range(n) if not visited[i])
