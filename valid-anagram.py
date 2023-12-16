class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of the strings are not equal, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Create a dictionary to store the frequency of each character in the first string
        d = {}
        for i in s:
            if i in d:
                d[i] += 1  # If the character is already in the dictionary, increment its count
            else:
                d[i] = 1  # If the character is not in the dictionary, add it with a count of 1

        # Iterate over the second string
        for i in t:
            if i in d:
                d[i] -= 1  # If the character is in the dictionary, decrement its count
            else:
                d[i] = 1  # If the character is not in the dictionary, add it with a count of 1

        # If any character has a non-zero count in the dictionary, the strings are not anagrams
        for i in d:
            if d[i] != 0:
                return False

        # If we have not returned False by this point, the strings are anagrams
        return True
