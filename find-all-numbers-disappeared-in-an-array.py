from typing import *

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        uniq = set(nums)
        result = []

        for j in range(1, len(nums) + 1):
            if j not in uniq:
                result.append(j)

        return result