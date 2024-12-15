from typing import *
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        
        def dist(o, a):
            return (a[0] - o[0]) ** 2 + (a[1] - o[1]) ** 2
        
        trees.sort(key=lambda x: (x[0], x[1]))
        n = len(trees)
        hull = []
        for i in range(n):
            while len(hull) >= 2 and cross(hull[-2], hull[-1], trees[i]) < 0:
                hull.pop()
            hull.append(trees[i])
        
        for i in range(n - 1, -1, -1):
            while len(hull) >= 2 and cross(hull[-2], hull[-1], trees[i]) < 0:
                hull.pop()
            hull.append(trees[i])
        
        return list(set(map(tuple, hull)))