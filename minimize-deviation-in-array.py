from typing import *
from heapq import heappush, heapify, heappushpop

class Solution:
    def minimumDeviation(self, nums):
        
        heap = []
        heapify(heap)
        
        min_elt = 1e12
        
        for c in nums:
            if c % 2 != 0:
                min_elt = min(min_elt, 2 * c)
                heappush(heap, -c * 2)
            else:
                min_elt = min(min_elt, c)
                heappush(heap, -c)
                
        min_deviation = 1e12
        
        while heap[0] % 2 == 0:
            
            min_deviation = min(min_deviation, -heap[0] - min_elt)
            
            if min_deviation == 1:
                return min_deviation
            
            min_elt = min(min_elt, - heap[0] // 2)
            
            heappushpop(heap, heap[0] // 2)
        
        return min(min_deviation, -heap[0] - min_elt)