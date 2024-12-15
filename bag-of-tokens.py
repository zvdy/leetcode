from typing import *
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        while tokens:
            if tokens[0] <= power:
                power -= tokens.pop(0)
                score += 1
            elif score > 0 and len(tokens) > 1:
                power += tokens.pop()
                score -= 1
            else:
                break
        return score