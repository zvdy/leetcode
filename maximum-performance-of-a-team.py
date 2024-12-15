from typing import *
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # Sort by efficiency
        engineers = sorted(zip(efficiency, speed), reverse=True)
        speed_heap = []
        speed_sum = 0
        perf = 0
        
        for e, s in engineers:
            if len(speed_heap) > k - 1:
                speed_sum -= heapq.heappop(speed_heap)
            heapq.heappush(speed_heap, s)
            
            speed_sum += s
            perf = max(perf, speed_sum * e)
            
        return perf % (10**9 + 7)