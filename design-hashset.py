from typing import *
from bisect import bisect_right as br


class MyHashSet:

    def __init__(self):
        self.set = []

    def add(self, key: int) -> None:
        if self.set:
            idx = br(self.set, key)
            if self.set[idx-1] == key:
                return
            self.set.insert(idx, key)
        else:
            self.set.append(key)
        
    def remove(self, key: int) -> None:
        if self.set:
            idx = br(self.set, key)
            if self.set[idx-1] == key:
                self.set.pop(idx-1)
        return
        

    def contains(self, key: int) -> bool:
        if self.set:
            idx = br(self.set, key)
            if self.set[idx-1] == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)