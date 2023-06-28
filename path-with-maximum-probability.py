class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
            graph = collections.defaultdict(list)
            for i, edge in enumerate(edges):
                graph[edge[0]].append((edge[1], succProb[i]))
                graph[edge[1]].append((edge[0], succProb[i]))
            
            pq = [(-1, start)]
            visited = set()
            while pq:
                prob, node = heapq.heappop(pq)
                if node == end:
                    return -prob
                if node in visited:
                    continue
                visited.add(node)
                for nei, nei_prob in graph[node]:
                    heapq.heappush(pq, (prob * nei_prob, nei))
            return 0