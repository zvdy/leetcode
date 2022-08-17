class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        pq = [(0, K)]
        seen = set()
        while pq:
            d, u = heapq.heappop(pq)
            if u in seen:
                continue
            seen.add(u)
            if len(seen) == N:
                return d
            for v, w in graph[u]:
                heapq.heappush(pq, (d + w, v))
        return -1