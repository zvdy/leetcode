from typing import *
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Initialize the result list with 0s
        N = len(deck)
        result = [0] * N
        
        # Sort the deck in ascending order
        deck.sort()
        
        # Call the helper function to fill the result list
        self.everyOther(deck, result, 0, 0, False)
        
        # Return the result list
        return result

    def everyOther(self, deck: List[int], result: List[int], indexInDeck: int, indexInResult: int, skip: bool) -> None:
        # Get the length of the deck
        N = len(deck)
        
        # If the index in the deck has reached the end, return
        if indexInDeck == N:
            return
        
        # Loop through the result list
        while indexInResult < N:
            # If the current position in the result list is 0, it's empty
            if result[indexInResult] == 0:
                # If we're not skipping, fill the position with the current card in the deck
                result[indexInResult] = deck[indexInDeck] if not skip else result[indexInResult - 1]
                
                # Move to the next card in the deck
                indexInDeck += 1
                
                # Toggle the skip flag
                skip = not skip
            
            # Move to the next position in the result list
            indexInResult += 1
        
        # Recursively call the function with the updated indices and skip flag
        self.everyOther(deck, result, indexInDeck, 0, skip)
