from typing import *
class Solution:
    def partitionString(self, s: str) -> int:
        
        # initialize the result
        result = 0

        # initialize the set of characters
        char_set = set()

        # iterate through the characters in the string
        for char in s:

            # if the character is not in the set
            if char not in char_set:

                # add the character to the set
                char_set.add(char)

            # otherwise
            else:

                # increment the result
                result += 1

                # reset the set
                char_set = set()

                # add the character to the set
                char_set.add(char)

        # increment the result
        result += 1

        # return the result
        return result