from typing import *
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for num in nums:
            if num==0:
                count+=1
            else:
                res+=count*(count+1)//2
                count = 0
        if count:
            res+=count*(count+1)//2
        return res

            