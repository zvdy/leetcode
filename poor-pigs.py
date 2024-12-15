from typing import *
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # initialize the number of pigs to 0
        pigs = 0
        # while the number of tests a pig can do before dying plus 1, raised to the power of the number of pigs,
        # is less than the number of buckets, keep adding pigs
        while (minutesToTest // minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        # return the number of pigs needed to determine which bucket is poisoned
        return pigs