class MyCalendarThree:

    def __init__(self):
        self.events = []


    def book(self, start: int, end: int) -> int:
        self.events.append((start, 1))
        self.events.append((end, -1))
        self.events.sort()
        active = 0
        ans = 0
        for _, delta in self.events:
            active += delta
            ans = max(ans, active)
        return ans
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)