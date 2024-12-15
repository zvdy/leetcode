from typing import *
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Initialize two empty lists to store the winners with 0 and 1 losses respectively
        ans = [[] for _ in range(2)]
        
        # Create a counter to keep track of the number of losses for each player
        lossesCount = Counter()
        
        # Iterate over each match
        for winner, loser in matches:
            # If the winner is not in the lossesCount dictionary, initialize their loss count to 0
            if winner not in lossesCount:
                lossesCount[winner] = 0
            # Increment the loss count for the loser
            lossesCount[loser] += 1
        
        # Iterate over each player and their corresponding loss count
        for player, nLosses in lossesCount.items():
            # If the player has less than 2 losses, add them to the corresponding list
            if nLosses < 2:
                ans[nLosses].append(player)
        
        # Sort the lists of winners with 0 and 1 losses in ascending order
        return [sorted(ans[0]), sorted(ans[1])]