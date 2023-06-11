class SnapshotArray:

    def __init__(self, length: int):
        self.arr = {}
        self.snaps = {}
        self.change = True
        

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val
        self.change = True

    def snap(self) -> int:
        snap_id = len(self.snaps)
        if self.change:
            self.snaps[snap_id] = self.arr.copy()
            self.change = False
        else:
            self.snaps[snap_id] = self.snaps[snap_id-1]
        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        return self.snaps[snap_id].get(index, 0)
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)