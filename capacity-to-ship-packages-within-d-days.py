from typing import *
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(weights, days, capacity):
            day = 0
            current = 0
            for weight in weights:
                if weight > capacity:
                    return False
                if current + weight > capacity:
                    day += 1
                    current = 0
                current += weight
            if current > 0:
                day += 1
            return day <= days
        
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            if canShip(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        return left