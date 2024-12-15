from typing import *
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
            def binary_search(l, r, target, mountain_arr, asc):
                while l <= r:
                    mid = (l + r) // 2
                    mid_val = mountain_arr.get(mid)
                    if mid_val == target:
                        return mid
                    elif mid_val < target:
                        if asc:
                            l = mid + 1
                        else:
                            r = mid - 1
                    else:
                        if asc:
                            r = mid - 1
                        else:
                            l = mid + 1
                return -1
            
            def find_peak(l, r, mountain_arr):
                while l < r:
                    mid = (l + r) // 2
                    if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                        l = mid + 1
                    else:
                        r = mid
                return l
            
            n = mountain_arr.length()
            peak = find_peak(0, n - 1, mountain_arr)
            left = binary_search(0, peak, target, mountain_arr, True)
            if left != -1:
                return left
            right = binary_search(peak + 1, n - 1, target, mountain_arr, False)
            return right