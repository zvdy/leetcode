from typing import *
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        if not order:
            return s
        if not s:
            return s
        order_map = {}
        for i in range(len(order)):
            order_map[order[i]] = i
        s = list(s)
        s.sort(key=lambda x: order_map.get(x, len(order)))
        return ''.join(s)