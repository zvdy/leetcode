from typing import *
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        max_index, min_index = -1,-1
        count = 0
        i,restart = 0,0

        while i<len(nums):
            if nums[i]<minK or nums[i]>maxK:
                restart = i+1
                max_index, min_index = -1,-1
            if nums[i]==minK:
                min_index = i
            if nums[i]==maxK:
                max_index = i

        
            c = 1 + min(max_index,min_index) - restart
            count += c if c>=0 else 0

            i += 1
        
        return count

