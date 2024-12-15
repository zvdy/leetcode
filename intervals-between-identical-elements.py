from typing import *
from collections import defaultdict


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        index = defaultdict(list)
        for i, a in enumerate(arr):
            index[a].append(i)
        n = len(arr)
        res = [0]*n
        for k in index:
            cur = 0
            for j in range(1, len(index[k])):
                cur += index[k][j] - index[k][0]
            res[index[k][0]] = cur
            left, right = 1, len(index[k]) - 1
            for j in range(1, len(index[k])):
                cur += -(right - left)*(index[k][j] - index[k][j-1])
                res[index[k][j]] = cur
                left += 1
                right -= 1
        return res


