from typing import *


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        t = sorted(nums)  # sort in order to get a descending amount of higher nums
        d = {}  # dictionary to ignore dups

        for i, num in enumerate(t):
            if num not in d:
                d[num] = i  # append all uniq nums to the dictionary
        r = []

        for i in nums:
            r.append(d[i])

        return r
