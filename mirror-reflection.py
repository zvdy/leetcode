from typing import *
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lcm = p * q // gcd(p, q)
        boxes = lcm // p
        if boxes % 2 == 0:
            return 0
        if(lcm // q) % 2 == 0:
            return 2
        return 1