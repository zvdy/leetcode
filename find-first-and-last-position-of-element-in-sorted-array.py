from typing import *
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(lo, hi, left):
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] > target or (left and target == nums[mid]):
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        lo = search(0, len(nums), True)
        if lo == len(nums) or nums[lo] != target:
            return [-1, -1]
        return [lo, search(lo, len(nums), False) - 1]