from typing import *
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        answer = [-1 for _ in range(n)]
        curr_sum = 0
        length = k+k+1
        if length > n:
            return answer
        for i in range(0,length):
            curr_sum+=nums[i]
        answer[k] = curr_sum//length
        for i in range(k+1,n-k):
            curr_sum+=nums[i+k]
            curr_sum-=nums[i-k-1]
            answer[i] = curr_sum//length
        return answer