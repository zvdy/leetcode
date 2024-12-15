from typing import *
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        count = 0
        prev_color = 0
        for i in range(1, len(colors)):
            # Check if the current color is the same as the previous color
            if colors[i] == colors[prev_color]:
                # If the time needed for the current color is greater than the time needed for the previous color,
                # add the time needed for the previous color to the count and update the previous color index
                if neededTime[i] > neededTime[prev_color]:
                    count += neededTime[prev_color]
                    prev_color = i
                # Otherwise, add the time needed for the current color to the count
                else:
                    count += neededTime[i]
            else:
                # If the current color is different from the previous color, update the previous color index
                prev_color = i
            
        return count
