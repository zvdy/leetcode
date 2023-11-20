class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Initialize variables to keep track of the last index at which each type of garbage was seen
        lm = 0  # Last index at which "M" was seen
        lg = 0  # Last index at which "G" was seen
        lp = 0  # Last index at which "P" was seen
        ans = 0  # Variable to store the total time needed to collect all the garbage

        # Iterate through each house
        for i in range(len(garbage)):
            # Update the last index for each type of garbage
            if "G" in garbage[i]:
                lg = i
            if "P" in garbage[i]:
                lp = i
            if "M" in garbage[i]:
                lm = i
            # Add the length of the current garbage assortment to the total time
            ans += len(garbage[i])

        # Add the travel time from the starting house to the last index of each type of garbage
        ans += sum(travel[:lm]) + sum(travel[:lg]) + sum(travel[:lp])

        # Return the total time needed to collect all the garbage
        return ans