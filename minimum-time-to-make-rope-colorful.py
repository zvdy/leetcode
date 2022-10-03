class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        count = 0
        prev_color = 0
        for i in range (1, len(colors)):
            if colors[i] == colors[prev_color]:
                if neededTime[i] > neededTime[prev_color]:
                    count += neededTime[prev_color]
                    prev_color = i
                else:
                    count += neededTime[i]
            else:
                prev_color = i
            
        return count