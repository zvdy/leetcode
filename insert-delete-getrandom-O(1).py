from typing import *
from collections import defaultdict
from random import randint

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []  # List to store the values
        self.valToIndex = defaultdict(int)  # Dictionary to map values to their indices

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.valToIndex:
            return False

        self.valToIndex[val] = len(self.vals)  # Add the value and its index to the dictionary
        self.vals.append(val)  # Append the value to the list
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.valToIndex:
            return False

        index = self.valToIndex[val]  # Get the index of the value
        self.valToIndex[self.vals[-1]] = index  # Update the index of the last value in the list
        del self.valToIndex[val]  # Remove the value from the dictionary
        self.vals[index] = self.vals[-1]  # Replace the value at the index with the last value in the list
        self.vals.pop()  # Remove the last value from the list
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = randint(0, len(self.vals) - 1)  # Generate a random index
        return self.vals[index]  # Return the value at the random index

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
