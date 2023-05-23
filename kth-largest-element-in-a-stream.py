class KthLargest:

    def __init__(self, k: int, nums: List[int]):
            self.k = k
            self.nums = nums
            self.nums.sort()
            self.nums = self.nums[::-1]
            self.nums = self.nums[:k]
            self.nums.sort()
            self.nums = self.nums[::-1]
            print(self.nums)


    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            self.nums.append(val)
            self.nums.sort()
            self.nums = self.nums[::-1]
        elif val > self.nums[-1]:
            self.nums[-1] = val
            self.nums.sort()
            self.nums = self.nums[::-1]
        return self.nums[-1]
    
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)