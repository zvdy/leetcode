from typing import *
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        start = 0
        end = len(nums)-1
        while start<end:
            left = start+1
            right = end-1
            currentClosest = float('inf')
            while left<=right:
                mid = (left+right)//2
                sum3 = nums[start]+nums[end]+nums[mid]
                
                if abs(target-sum3)<abs(target-currentClosest):
                    currentClosest = sum3
                if sum3>target:
                    right = mid-1
                else:
                    left = mid+1
            if abs(target-currentClosest)<abs(target-closest):
                    closest = currentClosest
            if currentClosest>target:
                end-=1
            else:
                start+=1
        return closest