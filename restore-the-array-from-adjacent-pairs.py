from typing import *
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # create a dictionary to represent the graph
        graph = defaultdict(list)
        # iterate through the adjacent pairs and add them to the graph
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        # find the starting node of the array
        start = None
        for u, v in graph.items():
            if len(v) == 1:
                start = u
                break
        # initialize the result array with the starting node
        res = [start]
        # keep track of the nodes that have been seen
        seen = set()
        seen.add(start)
        # iterate through the graph to restore the array
        while len(res) < len(adjacentPairs) + 1:
            for v in graph[start]:
                if v not in seen:
                    res.append(v)
                    seen.add(v)
                    start = v
                    break
        # return the restored array
        return res