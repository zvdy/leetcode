class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Initialize arrays to store the index of characters in the strings
        indexS = [0] * 200
        indexT = [0] * 200
        
        # Get the length of both strings
        length = len(s)
        
        # If the lengths of the two strings are different, they can't be isomorphic
        if length != len(t):
            return False
        
        # Iterate through each character of the strings
        for i in range(length):
            # Check if the index of the current character in string s is different from the index of the corresponding character in string t
            if indexS[ord(s[i])] != indexT[ord(t[i])]:
                return False
            
            # Update the position of the current character in string s
            indexS[ord(s[i])] = i + 1
            
            # Update the position of the current character in string t
            indexT[ord(t[i])] = i + 1
        
        # If the loop completes without returning false, strings are isomorphic
        return True
