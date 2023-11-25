class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # Sort the list
        piles.sort()
        
        # Initialize the result variable
        res = 0
        
        # Iterate over the range of the length of the list
        for i in range(len(piles)//3, len(piles), 2):
            # Add the second element from the end to the result variable
            res += piles[i]
        
        # Return the result variable
        return res