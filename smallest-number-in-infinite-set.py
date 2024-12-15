from typing import *
from heapq import heappush, heappop

class SmallestInfiniteSet:

    def __init__(self):
        self._added_back = []
        self._least_not_popped = 1
        self._removed = set()

    def popSmallest(self) -> int:
        if self._added_back and self._added_back[0] <= self._least_not_popped:
            res = heappop(self._added_back)
            if res == self._least_not_popped:
                self._least_not_popped += 1
        else:
            res = self._least_not_popped
            self._least_not_popped += 1

        if res in self._removed:
            return self.popSmallest()

        self._removed.add(res)

        return res

    def addBack(self, num: int) -> None:
        self._removed.discard(num)
        heappush(self._added_back, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)