class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = sorted(zip(profits, capital), key=lambda x: x[1])
        heap = []
        i = 0
        for _ in range(k):
            while i < n and projects[i][1] <= w:
                heapq.heappush(heap, -projects[i][0])
                i += 1
            if heap:
                w -= heapq.heappop(heap)
        return w