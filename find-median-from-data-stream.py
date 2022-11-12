class MedianFinder:

    def __init__(self):
        self.max = []
        self.min = []

    def addNum(self, num: int) -> None:
        if not self.max or num <= -self.max[0]:
            heapq.heappush(self.max, -num)
        else:
            heapq.heappush(self.min, num)
        if len(self.max) > len(self.min) + 1:
            heapq.heappush(self.min, -heapq.heappop(self.max))
        elif len(self.min) > len(self.max):
            heapq.heappush(self.max, -heapq.heappop(self.min))

        

    def findMedian(self) -> float:
        if len(self.max) == len(self.min):
            return (-self.max[0] + self.min[0]) / 2
        else:
            return -self.max[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()