from typing import *
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Calculate the time it takes for each monster to reach the city
        # by dividing the distance by the speed for each monster
        # Sort the resulting list in ascending order
        monsters = sorted([d / s for d, s in zip(dist, speed)])
        
        # Iterate over the sorted list of monsters
        for i, monster in enumerate(monsters):
            # If the time it takes for a monster to reach the city is less than or equal to the current time (i),
            # it means the monster has reached the city before it could be eliminated
            # So, return the number of monsters eliminated so far (i)
            if monster <= i:
                return i
                
        # If all monsters are eliminated before they could reach the city,
        # return the total number of monsters
        return len(monsters)