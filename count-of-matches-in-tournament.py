class Solution:
    # Function to calculate the number of matches in the tournament
    def numberOfMatches(self, n: int) -> int:
        # Initialize the number of matches
        matches = 0
        
        # Loop until there is only one team left
        while n > 1:
            # If the number of teams is even, each team gets paired with another team
            # If the number of teams is odd, one team randomly advances in the tournament, and the rest gets paired
            # Add the number of matches played in this round to the total number of matches
            matches += n // 2
            
            # Calculate the number of teams in the next round
            # If the number of teams is even, n / 2 teams advance to the next round
            # If the number of teams is odd, (n - 1) / 2 + 1 teams advance to the next round
            n = n // 2 + n % 2
        
        # Return the total number of matches played in the tournament
        return matches
