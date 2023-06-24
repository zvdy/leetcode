from functools import cache
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        n = len(rods)

        @cache
        def dp(i,d):
            if i == n and d == 0:
                return 0

            if i == n:
                return float(-inf)
            return max(
                dp(i+1, d), 
                rods[i] + dp(i+1, d+rods[i]),
                rods[i] + dp(i+1, d-rods[i]) 
            )
        return dp(0,0) // 2