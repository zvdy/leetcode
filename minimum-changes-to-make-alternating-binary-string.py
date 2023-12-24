class Solution:
    def minOperations(self, s: str) -> int:
        # Number of Changes Required
        changes = 0

        # Check Every Character in the String
        for i in range(len(s)):
            # If the Character is at an Even Position
            if i % 2 == 0:
                # If the Character is '1'
                if s[i] == '1':
                    # Increment the Number of Changes Required
                    changes += 1
            # If the Character is at an Odd Position
            else:
                # If the Character is '0'
                if s[i] == '0':
                    # Increment the Number of Changes Required
                    changes += 1
        
        # Return the Minimum Number of Changes Required
        return min(changes, len(s) - changes)