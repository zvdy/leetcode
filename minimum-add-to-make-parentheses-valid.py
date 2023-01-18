class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        right = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left + right