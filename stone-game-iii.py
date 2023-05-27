class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def dp(i=0) -> int:
            if i >= len(stoneValue):
                return 0
            return max(sum(stoneValue[i: i + x]) - dp(i + x) for x in range(1, 4)) 
        return ["Tie", "Alice", "Bob"][(dp() > 0) - (dp() < 0)]