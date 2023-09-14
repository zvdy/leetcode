class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)
        for start in graph:
            graph[start].sort(reverse=True)
        stack = ["JFK"]
        res = []
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            res.append(stack.pop())
        return res[::-1]