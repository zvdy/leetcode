class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.map = [None] * self.size

    def hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        if not self.map[index]:
            self.map[index] = ListNode(key, value)
        else:
            cur = self.map[index]
            while cur:
                if cur.key == key:
                    cur.val = value
                    return
                if not cur.next:
                    break
                cur = cur.next
            cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        cur = self.map[index]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        cur = prev = self.map[index]
        if not cur:
            return
        if cur.key == key:
            self.map[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.key == key:
                    prev.next = cur.next
                    break
                cur, prev = cur.next, prev.next
                
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)