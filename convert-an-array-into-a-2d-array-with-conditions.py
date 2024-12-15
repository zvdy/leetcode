from typing import *
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = defaultdict(int)
        ans = []

        for c in nums:
            if freq[c] >= len(ans):
                ans.append([])

            # Store the integer in the list corresponding to its current frequency.
            ans[freq[c]].append(c)
            freq[c] += 1

        return ans
