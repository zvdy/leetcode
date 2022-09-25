class MyCircularQueue:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.k = k
        self.q = [None] * k
        self.rear = k - 1
  
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
  
        self.rear = (self.rear + 1) % self.k
        self.q[self.rear] = value
        self.size += 1
        return True
  
    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
  
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True
  
    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return -1 if self.isEmpty() else self.q[self.front]
  
    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return -1 if self.isEmpty() else self.q[self.rear]
  
    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0
  
    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.k
  
    def __str__(self):
        return str(self.q)
  
    k = None
    q = None
    size = 0
    front = 0
    rear = None