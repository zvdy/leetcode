class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @cache
        def dp(l, r):
            ans = float('inf')
            for cut in cuts:
                if l < cut < r:
                    ans = min(ans, r-l+dp(l,cut)+dp(cut,r))
            if ans == float('inf'):
                return 0
            return ans
        return dp(0,n)
        