from typing import *
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_count = max(counts.values())
        if max_count > (len(s) + 1) // 2:
            return ""
        result = [None] * len(s)
        even_index, odd_index = 0, 1
        half_length = len(s) // 2
        for letter, count in counts.items():
            while count > 0 and count <= half_length and odd_index < len(s):
                result[odd_index] = letter
                count -= 1
                odd_index += 2
            while count > 0:
                result[even_index] = letter
                count -= 1
                even_index += 2
        return "".join(result)