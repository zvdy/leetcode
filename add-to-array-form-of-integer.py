from typing import *
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = int(''.join(map(str, num)))
        return list(map(int, str(num + k)))