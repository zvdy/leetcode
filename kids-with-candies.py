from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        get_max = max(candies)
        for i in range(len(candies)):
            value = candies[i]
            if (value + extraCandies) >= get_max:
                result.append(True)
            else:
                result.append(False)
        return result
    